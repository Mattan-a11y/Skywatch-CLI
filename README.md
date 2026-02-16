# Skywatch CLI ☁️

A beautiful, modern terminal weather application that brings real-time weather data from anywhere in the world directly to your command line. No API key required!

## 🎯 Features

- **🌍 Global Coverage**: Weather for any city on Earth
- **🎨 Beautiful UI**: Styled terminal output using Rich library
- **⚡ Fast & Free**: Uses Open-Meteo API (no registration needed)
- **🌡️ Unit Support**: Both metric (°C, m/s) and imperial (°F, mph)
- **🧭 Wind Direction**: Compass direction with degree display
- **📍 Geocoding**: Smart location search with coordinates
- **⌨️ Interactive**: Command-line arguments or interactive prompts
- **🎭 Emoji Support**: Weather icons in your terminal
- **⏱️ Live Status**: Animated loading indicators

## 📋 Requirements

- Python 3.7 or higher
- `requests` library
- `rich` library (for beautiful terminal output)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/skywatch-cli.git
cd skywatch-cli

# Install dependencies
pip install requests rich

# Make executable (optional, Linux/macOS)
chmod +x Skywatch_CLI.py

# Run it!
python Skywatch_CLI.py
```

### Alternative: Install via requirements.txt

```bash
pip install -r requirements.txt
```

Create `requirements.txt`:
```
requests>=2.28.0
rich>=13.0.0
```

## 💻 Usage

### Quick Start

```bash
# Interactive mode - will prompt for city
python Skywatch_CLI.py

# Direct city lookup
python Skywatch_CLI.py "Lund"
python Skywatch_CLI.py "Stockholm"
python Skywatch_CLI.py "New York"

# With imperial units
python Skywatch_CLI.py "London" --units imperial

# With metric units (default)
python Skywatch_CLI.py "Tokyo" --units metric
```

### Command-Line Options

```bash
usage: Skywatch_CLI.py [-h] [--units {metric,imperial}] [city]

SKYWATCH CLI – Live weather data in your terminal

positional arguments:
  city                  City name, e.g. 'Lund' or 'Stockholm'

optional arguments:
  -h, --help            show this help message and exit
  --units {metric,imperial}
                        Units: metric (°C,m/s) or imperial (°F,mph)
```

## 📊 Example Output

```
╔═══════════════════════════════════════════════════════╗
║         🌦️  SKYWATCH CLI  v1.0                        ║
║    Real-time Weather for Every City on Earth         ║
╚═══════════════════════════════════════════════════════╝

🔍 Looking up location...

╭─────────────────────────────────────────────────────────────╮
│ ☁️  Lund, Skåne län, Sweden                                │
│ Coords 55.7047, 13.1910 • As of 14:30, Feb 16 2024       │
╰─────────────────────────────────────────────────────────────╯

╭───────────── Current Weather ──────────────╮
│       5.2°C          Partly cloudy          │
│                      SW (225°), 4.5 m/s     │
╰─────────────────────────────────────────────╯

    Powered by Open-Meteo – no API key needed 🌎
```

### Imperial Units Example

```bash
$ python Skywatch_CLI.py "Miami" --units imperial

╔═══════════════════════════════════════════════════════╗
║         🌦️  SKYWATCH CLI  v1.0                        ║
║    Real-time Weather for Every City on Earth         ║
╚═══════════════════════════════════════════════════════╝

╭─────────────────────────────────────────────────────────────╮
│ ☁️  Miami, Florida, United States                          │
│ Coords 25.7743, -80.1937 • As of 15:45, Feb 16 2024      │
╰─────────────────────────────────────────────────────────────╯

╭───────────── Current Weather ──────────────╮
│      78.4°F          Clear sky              │
│                      E (90°), 11.2 mph      │
╰─────────────────────────────────────────────╯

    Powered by Open-Meteo – no API key needed 🌎
```

## 🌤️ Weather Codes

The app translates numerical weather codes into readable descriptions:

| Code | Description |
|------|-------------|
| 0 | Clear sky |
| 1 | Mainly clear |
| 2 | Partly cloudy |
| 3 | Overcast |
| 45-48 | Fog |
| 51-55 | Drizzle (light to dense) |
| 61-65 | Rain (light to heavy) |
| 71-75 | Snow (light to heavy) |
| 80-81 | Rain showers |
| 95-99 | Thunderstorm |

## 🎓 Use Cases

### Daily Weather Check
```bash
# Add to your .bashrc or .zshrc
alias weather='python ~/skywatch-cli/Skywatch_CLI.py "Lund"'

# Now just type:
weather
```

### Travel Planning
```bash
# Check weather in multiple cities
python Skywatch_CLI.py "Paris"
python Skywatch_CLI.py "Berlin"
python Skywatch_CLI.py "Rome"
```

### System Monitoring
```bash
# Add to your system status scripts
python Skywatch_CLI.py "$(curl -s ipinfo.io/city)"
```

### Remote Server Status
```bash
# SSH into server and check local weather
ssh user@server 'python skywatch.py "Stockholm"'
```

## 🔧 Advanced Usage

### Create an Alias

**Linux/macOS (bash/zsh):**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias weather='python3 /path/to/Skywatch_CLI.py'
alias w='python3 /path/to/Skywatch_CLI.py'

# Reload config
source ~/.bashrc  # or ~/.zshrc

# Now use it:
weather "Lund"
w "Stockholm"
```

**Windows (PowerShell):**
```powershell
# Add to $PROFILE
function weather { python C:\path\to\Skywatch_CLI.py $args }

# Use it:
weather "Lund"
```

### Integration with Other Tools

**tmux status bar:**
```bash
# In .tmux.conf
set -g status-right '#(python ~/skywatch-cli/Skywatch_CLI.py "Lund" | grep "°C")'
```

**Conky system monitor:**
```bash
${exec python ~/skywatch-cli/Skywatch_CLI.py "Lund"}
```

## 🛠️ Customization

### Modify the Banner

Edit the `print_banner()` function to customize the ASCII art:

```python
def print_banner():
    title = "🌦️  YOUR CUSTOM NAME"
    subtitle = "Your Custom Tagline"
    # ... rest of the code
```

### Add More Data Points

The Open-Meteo API provides many more parameters. You can extend the script:

```python
params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": "true",
    "hourly": "temperature_2m,precipitation",  # Add hourly data
    "daily": "temperature_2m_max,temperature_2m_min",  # Add daily forecast
    "timezone": timezone,
}
```

### Change Color Scheme

Modify the Rich styling throughout the code:

```python
# Change from cyan to green
console.print(box_top, style="green")
console.print(f"║ {title.center(line_len - 2)}  ║", style="bold green")
```

## 🔍 Troubleshooting

### "Could not find location"
- Check spelling of city name
- Try adding country: `"Lund, Sweden"`
- Use English names: `"Copenhagen"` not `"København"`

### "Could not fetch weather"
- Check internet connection
- Open-Meteo API might be temporarily down
- Try again in a few seconds

### "ModuleNotFoundError: No module named 'rich'"
```bash
pip install rich
```

### Unicode/Emoji Issues (Windows)
```bash
# Try running with UTF-8 encoding
chcp 65001
python Skywatch_CLI.py "Lund"
```

### Permission Denied (Linux/macOS)
```bash
chmod +x Skywatch_CLI.py
./Skywatch_CLI.py "Lund"
```

## 🌟 Features in Detail

### Geocoding
- Uses Open-Meteo's geocoding API
- Returns top 5 matches (uses first one)
- Provides coordinates, country, and timezone
- No API key needed

### Weather Data
- Current temperature
- Weather condition (clear, cloudy, rain, etc.)
- Wind speed and direction
- Timestamp with timezone conversion
- All data refreshed in real-time

### Terminal UI
- Styled with Rich library
- Color-coded information
- Box borders and panels
- Animated loading spinners
- Aligned and centered text
- Emoji support (if terminal supports it)

## 🔮 Future Enhancements

- [ ] 7-day forecast view
- [ ] Hourly weather predictions
- [ ] Weather alerts and warnings
- [ ] Historical weather data
- [ ] Multiple city comparison
- [ ] Save favorite locations
- [ ] Graph/chart visualization (using plotext)
- [ ] Configuration file support
- [ ] Weather notifications (desktop/mobile)
- [ ] Integration with calendar apps
- [ ] Air quality index (AQI)
- [ ] UV index
- [ ] Sunrise/sunset times
- [ ] Moon phase

## 📊 Technical Details

### APIs Used
- **Geocoding**: https://geocoding-api.open-meteo.com/v1/search
- **Weather**: https://api.open-meteo.com/v1/forecast

### Dependencies
- `requests`: HTTP requests to APIs
- `rich`: Terminal formatting and styling
- Standard library: `sys`, `argparse`, `time`, `datetime`

### Performance
- Geocoding: ~100-300ms
- Weather fetch: ~100-500ms
- Total runtime: ~500ms-1s (depending on network)

## ⚖️ Legal & Licensing

- **Open-Meteo API**: Free to use, CC BY 4.0 license
- **No API Key**: Completely free, no registration required
- **Fair Use**: API is rate-limited but generous for personal use
- **Attribution**: Data provided by Open-Meteo.com

## 💡 Pro Tips

1. **Create a Shell Function**:
```bash
w() { python ~/skywatch-cli/Skywatch_CLI.py "$@"; }
```

2. **Quick Multiple Locations**:
```bash
for city in "Lund" "Stockholm" "Gothenburg"; do
    python Skywatch_CLI.py "$city"
done
```

3. **Export to File**:
```bash
python Skywatch_CLI.py "Lund" > weather.txt
```

4. **Check Before Leaving**:
```bash
# Add to .zshrc
preexec() { weather "Lund"; }
```

5. **Combine with Other Commands**:
```bash
python Skywatch_CLI.py "$(curl -s ipinfo.io/city)" && notify-send "Weather Updated"
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Ideas:
- Add 7-day forecast
- Historical weather data
- Weather graphs with plotext
- Save/load favorite cities
- Configuration file support
- Weather alerts
- More detailed wind information
- Precipitation probability

## 👤 Author

Your Name
- GitHub: [@Mattan-a11y](https://github.com/Mattan-a11y)
- LinkedIn: [Matin Shahid](https://www.linkedin.com/in/matin-shahid-1b426a217/)

## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for the excellent free weather API
- [Rich](https://github.com/Textualize/rich) for beautiful terminal formatting
- Python community for amazing tools and libraries

## 📚 Related Projects

- [wttr.in](https://github.com/chubin/wttr.in) - Weather in your terminal (curl-based)
- [wego](https://github.com/schachmat/wego) - Weather app in Go
- [ansiweather](https://github.com/fcambus/ansiweather) - Shell script weather

## ⭐ Show Your Support

If this project helped you, please:
- ⭐ Star the repository
- 🐛 Report bugs via Issues
- 💡 Suggest new features
- 🔀 Submit pull requests
- 📢 Share with friends!

---

**Stay Weather-Aware! 🌤️**

*Made with ☕ and Python*
