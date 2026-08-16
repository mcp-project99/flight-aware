# Privacy notes

## Data the starter checker reads

- Local service status for names chosen by the user
- Free and total space for the local root filesystem
- CPU temperature only when the local operating system provides it

## Data it does not read or transmit

- Feeder identifiers
- Aircraft or receiver data
- Geographic location
- IP addresses or Wi-Fi settings
- FlightAware, ADS-B Exchange, or other account credentials
- API keys, notification tokens, or passwords

The starter checker makes no network requests. Its JSON output remains on the local device unless the user deliberately sends it somewhere.

## Safe configuration

Keep device-specific configuration in a local file ignored by Git, such as `config.local.toml`. Before publishing changes, review `git status` and the staged diff to ensure that no private information is included.
