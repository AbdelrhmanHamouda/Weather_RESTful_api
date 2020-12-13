import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# Jinja searches this 'templates' when it gets a request.
from services import report_service

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}
    # Render 'home/index.html'
    # The request object is needed by starlette and it is safe to pass it as it is.
    return templates.TemplateResponse('home/index.html', data)


@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
