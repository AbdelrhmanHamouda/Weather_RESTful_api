import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# Jinja searches this 'templates' when it gets a request.
templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/')
def index(request: Request):
    # Render 'home/index.html'
    # The request object is needed by starlette and it is safe to pass it as it is.
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
