"""
SKYWATCH CLI v1.0 — Stylish terminal weather app (Open-Meteo, no API key)
works anywhere 🌍
"""

from __future__ import annotations
import sys
import argparse
import requests
import time
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.align import Align
from rich.spinner import Spinner
from rich.prompt import Prompt
from rich.live import Live

console = Console()

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHERCODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Heavy showers",
    95: "Thunderstorm",
    99: "Severe thunderstorm",
}

# ─────────────────────────────────────────────────────────────
# ✨ Cool Banner
# ─────────────────────────────────────────────────────────────
def print_banner():
    # We’ll use a slightly shorter text width so borders match despite emoji width.
    line_len = 55
    line = "═" * line_len
    box_top = f"╔{line}╗"
    box_bottom = f"╚{line}╝"

    # Emoji stays inside, manually centered by adjusting spacing
    title = "🌦️  SKYWATCH CLI  v1.0"
    subtitle = "Real-time Weather for Every City on Earth"

    console.print()
    console.print(box_top, style="cyan")
    console.print(f"║ {title.center(line_len - 2)}  ║", style="bold cyan")
    console.print(f"║ {subtitle.center(line_len - 2)} ║", style="dim cyan")
    console.print(box_bottom, style="cyan")
    console.print()



# ─────────────────────────────────────────────────────────────
# 🌍 API helpers
# ─────────────────────────────────────────────────────────────
def geocode(city: str) -> Optional[dict]:
    params = {"name": city, "count": 5, "language": "en", "format": "json"}
    try:
        r = requests.get(GEOCODE_URL, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        if "results" not in data or not data["results"]:
            return None
        top = data["results"][0]
        return {
            "name": top.get("name"),
            "country": top.get("country"),
            "latitude": float(top.get("latitude")),
            "longitude": float(top.get("longitude")),
            "timezone": top.get("timezone", "auto"),
            "admin1": top.get("admin1", ""),
        }
    except Exception as e:
        console.log("[red]Geocoding error[/red]:", e)
        return None


def fetch_current_weather(lat: float, lon: float, timezone: str = "auto") -> Optional[dict]:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "timezone": timezone,
    }
    try:
        r = requests.get(WEATHER_URL, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        if "current_weather" not in data:
            return None
        return data["current_weather"]
    except Exception as e:
        console.log("[red]Weather fetch error[/red]:", e)
        return None


# ─────────────────────────────────────────────────────────────
# 💨 Utility functions
# ─────────────────────────────────────────────────────────────
def compass_direction(deg: float) -> str:
    dirs = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S",
            "SSW","SW","WSW","W","WNW","NW","NNW"]
    idx = int((deg + 11.25) / 22.5) % 16
    return dirs[idx]


from datetime import datetime

def prettify_output(location: dict, weather: dict, units: str = "metric"):
    # Prepare readable time
    raw_time = weather.get("time", "")
    try:
        dt = datetime.fromisoformat(raw_time)
        nice_time = dt.strftime("%H:%M, %b %d %Y")
    except Exception:
        nice_time = raw_time

    header = f":white_sun_behind_cloud:  [bold]{location['name']}{(', ' + location['admin1']) if location.get('admin1') else ''}[/bold], {location.get('country','')}"
    sub = f"[dim]Coords[/dim] {location['latitude']:.4f}, {location['longitude']:.4f} • [dim]As of[/dim] {nice_time}"
    title_panel = Panel(Align.left(f"{header}\n{sub}"), box=box.ROUNDED, padding=(0,1), border_style="bright_blue")
    console.print(title_panel)

    # Weather data
    temp = weather.get("temperature")
    wcode = int(weather.get("weathercode", -1))
    wtext = WEATHERCODE_MAP.get(wcode, f"Code {wcode}")
    wind_speed = weather.get("windspeed")
    wind_dir = weather.get("winddirection")

    temp_unit = "°C" if units == "metric" else "°F"
    speed_unit = "m/s" if units == "metric" else "mph"

    # Format main data cleanly
    temp_str = f"[bold magenta]{temp:.1f}{temp_unit}[/bold magenta]"
    condition_str = f"[dim]{wtext}[/dim]"
    wind_str = f"{compass_direction(wind_dir)} ({wind_dir:.0f}°), {wind_speed:.1f} {speed_unit}"

    # Table layout: left = temp, right = everything else
    table = Table.grid(expand=False)
    table.add_column(justify="center")
    table.add_column(justify="left", width=30)
    table.add_row(temp_str, condition_str)
    table.add_row("", wind_str)

    console.print(Panel(table, title="Current Weather", border_style="green", box=box.ROUNDED))
    console.print(Align.center("[dim]Powered by Open-Meteo — no API key needed 🌍[/dim]\n"))




# ─────────────────────────────────────────────────────────────
# 🚀 Main
# ─────────────────────────────────────────────────────────────
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="SKYWATCH CLI — Live weather data in your terminal")
    parser.add_argument("city", nargs="?", help="City name, e.g. 'Lund' or 'Stockholm'")
    parser.add_argument("--units", choices=["metric","imperial"], default="metric", help="Units: metric (°C,m/s) or imperial (°F,mph)")
    args = parser.parse_args()

    city = args.city or Prompt.ask("Enter city (e.g. Lund, SE)")

    with console.status("[bold cyan]🔍 Looking up location...[/bold cyan]", spinner="earth"):
        loc = geocode(city)
    if not loc:
        console.print(f"[red]Could not find location for[/red] [bold]{city}[/bold]. Try a more specific query.")
        console.print("[dim]Tip: Try `curl wttr.in/<city>` for a quick alt.[/dim]")
        sys.exit(1)

    with console.status("[bold blue]☁️  Fetching current weather...[/bold blue]", spinner="dots"):
        current = fetch_current_weather(loc["latitude"], loc["longitude"], timezone=loc.get("timezone","auto"))

    if not current:
        console.print("[red]Could not fetch weather — try again later.[/red]")
        sys.exit(2)

    if args.units == "imperial":
        current = current.copy()
        current["temperature"] = current["temperature"] * 9/5 + 32
        current["windspeed"] = current["windspeed"] * 2.2369362920544

    prettify_output(loc, current, units=args.units)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Aborted.[/bold red]")
        raise SystemExit(0)
