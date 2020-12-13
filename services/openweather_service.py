from typing import Optional

# This key will be set by the configure_apikeys function on startup
import requests

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    # Change the query based on the provided params
    if state:
        query = f'{city},{state},{country}'
    else:
        query = f'{city},{country}'

    # Construct the request url
    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&units={units}&appid={api_key}'

    # Send request
    response = requests.get(url)

    # Parse data from json to dict
    data = response.json()

    # extract the 'main' section
    forecast = data['main']

    # Return forecast
    return forecast
