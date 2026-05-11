# skywatch-cli

A terminal weather app built with Python. Shows current conditions for any city on Earth — no API key needed.

## Requirements

```bash
pip install requests rich
```

## Usage

```bash
# Interactive
python3 skywatch.py

# Pass city directly
python3 skywatch.py Stockholm
python3 skywatch.py "New York" --units imperial
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `city` | City name (quoted if multiple words) | Prompted if not given |
| `--units` | `metric` (°C, km/h) or `imperial` (°F, mph) | metric |

## How it works

Uses two free APIs from [Open-Meteo](https://open-meteo.com/):
- Geocoding API to convert city name → coordinates
- Weather API to fetch current conditions for those coordinates

No account, no key, no rate limits for personal use.

## Notes

- Wind speed is in km/h (metric) or mph (imperial)
- Weather codes follow the WMO standard — the full list is in the source
- If a city name is ambiguous, it picks the top result from the geocoder

## License

MIT

## Author

[@Mattan-a11y](https://github.com/Mattan-a11y) · [LinkedIn](https://www.linkedin.com/in/matin-shahid-1b426a217/)
