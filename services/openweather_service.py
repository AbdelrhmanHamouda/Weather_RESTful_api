from typing import Optional


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    query = f'{city},{country}'
    key = 132
    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={key}?units={units}'
    print(url)
