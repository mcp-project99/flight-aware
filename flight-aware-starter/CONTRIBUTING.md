# Contributing

Thank you for helping make volunteer ADS-B feeder monitoring safer and easier.

Please keep contributions privacy-first:

- Never commit feeder IDs, location information, IP addresses, Wi-Fi details, account names, logs, API keys, or notification credentials.
- Use synthetic examples in documentation and tests.
- Keep the default checker local-only and free of outbound network calls.
- Explain any new data collection or alert integration in `docs/PRIVACY.md`.

Before opening a pull request, run:

```bash
python -m unittest discover -s tests
```
