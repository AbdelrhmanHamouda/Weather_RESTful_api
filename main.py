import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    """
    This function is used to configure the service
    """
    configure_routing()
    configure_apikeys()


def configure_apikeys():
    """
    Use this function to get the API key
    """
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f'WARNING: {file} file not found, you cannot continue, please see settings_template.json')
        raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")
    with open('settings.json') as file_handler:
        settings = json.load(file_handler)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    # Opt in making fastAPI pick the 'static' dir to use it
    api.mount('/static', StaticFiles(directory='static'), name='static')
    # Setup routers
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8005, host='127.0.0.1')
else:
    configure()
