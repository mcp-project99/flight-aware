"""Local-only health checks. This module never makes network requests."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


def service_status(name: str) -> str:
    """Return a systemd service state without exposing device-specific data."""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", name],
            capture_output=True,
            check=False,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "unavailable"

    state = result.stdout.strip()
    return state or "unknown"


def cpu_temperature_c() -> Optional[float]:
    """Read a generic Linux thermal-zone value when one is available."""
    thermal_path = Path("/sys/class/thermal/thermal_zone0/temp")
    try:
        value = int(thermal_path.read_text(encoding="utf-8").strip())
    except (FileNotFoundError, OSError, ValueError):
        return None
    return round(value / 1000, 1)


def storage_summary(path: str = "/") -> Dict[str, float]:
    """Return only aggregate filesystem capacity information."""
    usage = shutil.disk_usage(path)
    gib = 1024**3
    return {
        "total_gib": round(usage.total / gib, 2),
        "free_gib": round(usage.free / gib, 2),
    }


def run_checks(services: Iterable[str]) -> Dict[str, Any]:
    """Build a local health report without identifiers or network activity."""
    return {
        "services": {service: service_status(service) for service in services},
        "storage": storage_summary(),
        "cpu_temperature_c": cpu_temperature_c(),
    }
