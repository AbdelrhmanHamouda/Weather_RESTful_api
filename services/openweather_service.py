from typing import Optional

# This key will be set by the configure_apikeys function on startup
api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    query = f'{city},{country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}?units={units}'
    print(url)
