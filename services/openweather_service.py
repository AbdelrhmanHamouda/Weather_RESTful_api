from typing import Optional, Tuple

# This library support async / await functionality.
import httpx
from httpx import Response

from infrastructure import weather_cache
from models.validation_error import ValidationError

# This key will be set by the configure_apikeys function on startup
api_key: Optional[str] = None


# TODO watch https://training.talkpython.fm/player/course/getting-started-with-fastapi/lecture/300603 at 3:30
async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    """
    Function responsible for getting the weather report.
    It looks at the cashed info first, if found, results are returned, if not, an API call is made.
    :param city: str, name of the city.
    :param state: (str - optional), name of the state.
    :param country: str, name of the country.
    :param units: str, unit system to use.
    :return: dict, weather forecast.
    """

    # Validate the provided parameters
    city, state, country, units = validate_units(city, state, country, units)

    # If forecast available in cache, return it.
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
        response: Response = await clint.get(url)
        if response.status_code != 200:
            raise ValidationError(response.text, status_code=response.status_code)

    # Parse data from json to dict
    data = response.json()

    # extract the 'main' section
    forecast = data['main']

    # Cache forecast
    weather_cache.set_weather(city, state, country, units, forecast)

    # Return forecast
    return forecast


def validate_units(city: str, state: Optional[str], country: Optional[str], units: str) -> \
        Tuple[str, Optional[str], str, str]:
    """
    Function to validate (and if needed raise errors) for provided parameters
    :param city: str, name of the city.
    :param state: (str - optional), name of the state.
    :param country: str, name of the country.
    :param units: str, unit system to use.
    :return: Tuple, modified and validated parameters
    """
    city = city.lower().strip()
    if not country:
        country = "us"
    else:
        country = country.lower().strip()

    if len(country) != 2:
        error = f"Invalid country: {country}. It must be a two letter abbreviation such as US or GB."
        raise ValidationError(status_code=400, error_message=error)

    if state:
        state = state.strip().lower()

    if state and len(state) != 2:
        error = f"Invalid state: {state}. It must be a two letter abbreviation such as CA or KS (use for US only)."
        raise ValidationError(status_code=400, error_message=error)

    if units:
        units = units.strip().lower()

    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f"Invalid units '{units}', it must be one of {valid_units}."
        raise ValidationError(status_code=400, error_message=error)

    return city, state, country, units
