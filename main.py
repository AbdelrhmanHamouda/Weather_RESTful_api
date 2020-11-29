import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home

api = fastapi.FastAPI()

# Opt in making fastAPI pick the 'static' dir to use it
api.mount('/static', StaticFiles(directory='static'), name='static')
# Setup routers
api.include_router(home.router)
api.include_router(weather_api.router)

if __name__ == '__main__':
    uvicorn.run(api, port=8005, host='127.0.0.1')
