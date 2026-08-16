# ADS-B Feeder Health Monitor

A privacy-first, local health checker for volunteer ADS-B feeder setups.

It checks the health of local services such as `piaware` and `dump1090`, available disk space, and CPU temperature. It does **not** read, send, or store feeder IDs, aircraft data, locations, IP addresses, Wi-Fi details, account credentials, or API keys.

> This is an independent community project. It is not affiliated with or endorsed by FlightAware.

## What it checks

- Whether configured local services are active
- Available disk space on the device
- CPU temperature when the operating system exposes it
- A machine-readable JSON report for monitoring or alerts

## Privacy model

The checker is local-first: it prints a report to standard output and makes no network requests. Optional alerting can be added later, but credentials must remain outside the repository and outside committed configuration files.

Read the [privacy notes](docs/PRIVACY.md) before configuring or contributing.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
adsb-feeder-health
```

## Configuration

The defaults check `piaware` and `dump1090-fa`. `config.example.toml` is documentation only: copy it to a private local filename if you need to track different service names. Do not commit device-specific configuration.

## Development

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome, especially support for additional local feeder services, safer alert integrations, documentation, and tests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
