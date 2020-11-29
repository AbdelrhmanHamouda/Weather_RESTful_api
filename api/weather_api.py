import fastapi

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather():
    return "some report"
