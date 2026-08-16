import unittest
from unittest.mock import patch

from feeder_health.checks import run_checks


class RunChecksTests(unittest.TestCase):
    @patch("feeder_health.checks.service_status", return_value="active")
    @patch("feeder_health.checks.storage_summary")
    @patch("feeder_health.checks.cpu_temperature_c", return_value=42.0)
    def test_report_contains_only_health_information(
        self, temperature, storage, status
    ):
        storage.return_value = {"total_gib": 16.0, "free_gib": 8.0}
        report = run_checks(["piaware"])

        self.assertEqual(report["services"], {"piaware": "active"})
        self.assertEqual(report["storage"]["free_gib"], 8.0)
        self.assertEqual(report["cpu_temperature_c"], 42.0)


if __name__ == "__main__":
    unittest.main()
