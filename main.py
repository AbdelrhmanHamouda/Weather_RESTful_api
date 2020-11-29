import fastapi
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates

api = fastapi.FastAPI()
# Jinja searches this 'templates' when it gets a request.
templates = Jinja2Templates('templates')


@api.get('/')
def index(request: Request):
    # Render 'home/index.html'
    # The request object is needed by starlette and it is safe to pass it as it is.
    return templates.TemplateResponse('home/index.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run(api, port=8005, host='127.0.0.1')
