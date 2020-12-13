import datetime
from typing import Optional, Tuple

__cache = {}
lifetime_in_hours = 1.0


def __create_key(city: str, state: str, country: str, units: str) -> Tuple[str, str, str, str]:
    """
    Function constructs a key based on the passed parameters.
    :param city: str, name of the city.
    :param state: (str - optional), name of the state.
    :param country: str, name of the country.
    :param units: str, unit system to use.
    :return: Tuple, containing a key representation.
    """
    if not city or not country or not units:
        raise Exception("City, country, and units are required!")

    if not state:
        state = ""

    return city.strip().lower(), state.strip().lower(), country.strip().lower(), units.strip().lower()


def get_weather(city: str, state: Optional[str], country: str, units: str) -> Optional[dict]:
    """
    Function to get a cashed value. If no value is found or it is too old, nothing will be returned.
    :param city: str, name of the city.
    :param state: (str - optional), name of the state.
    :param country: str, name of the country.
    :param units: str, unit system to use.
    :return: (dict or None), for weather info found in cache.
    """
    key = __create_key(city, state, country, units)
    data: dict = __cache.get(key)
    if not data:
        return None

    last = data['time']
    dt = datetime.datetime.now() - last
    if dt / datetime.timedelta(minutes=60) < lifetime_in_hours:
        return data['value']

    del __cache[key]
    return None


def set_weather(city: str, state: str, country: str, units: str, value: dict) -> None:
    """
    Function the populates a new entry to the __cache dict and performs a cleanup routine everytime it is called.
    :param city: str, name of the city.
    :param state: (str - optional), name of the state.
    :param country: str, name of the country.
    :param units: str, unit system to use.
    :param value: dict, to be passed to the __cache.
    :return:  None
    """
    key = __create_key(city, state, country, units)
    data = {
        'time': datetime.datetime.now(),
        'value': value
    }
    __cache[key] = data
    __clean_out_of_date()


def __clean_out_of_date() -> None:
    """
    Function when called will scan the __cache dict and delete all old data.
    :return: None
    """
    for key, data in list(__cache.items()):
        dt = datetime.datetime.now() - data.get('time')
        if dt / datetime.timedelta(minutes=60) > lifetime_in_hours:
            del __cache[key]
