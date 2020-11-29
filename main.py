import fastapi
import uvicorn
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

api = fastapi.FastAPI()
# Jinja searches this 'templates' when it gets a request.
templates = Jinja2Templates('templates')
# Opt in making fastAPI pick the 'static' dir to use it
api.mount('/static', StaticFiles(directory='static'), name='static')


@api.get('/')
def index(request: Request):
    # Render 'home/index.html'
    # The request object is needed by starlette and it is safe to pass it as it is.
    return templates.TemplateResponse('home/index.html', {'request': request})


@api.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')


@api.get('api/weather')
def weather():
    return "some report"


if __name__ == '__main__':
    uvicorn.run(api, port=8005, host='127.0.0.1')
