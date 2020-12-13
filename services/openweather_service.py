from typing import Optional

# This library support async / await functionality.
import httpx

from infrastructure import weather_cache

# This key will be set by the configure_apikeys function on startup
api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if forecast := weather_cache.get_weather(city, state, country, units):
        return forecast

    # Change the query based on the provided params
    if state:
        query = f'{city},{state},{country}'
    else:
        query = f'{city},{country}'

    # Construct the request url
    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&units={units}&appid={api_key}'

    async with httpx.AsyncClient() as clint:
        # Send request
        response = await clint.get(url)

    # Parse data from json to dict
    data = response.json()

    # extract the 'main' section
    forecast = data['main']

    weather_cache.set_weather(city, state, country, units, forecast)

    # Return forecast
    return forecast
