from typing import Optional

import fastapi
from fastapi import Depends

from models.Location import Location
from services import openweather_service

router = fastapi.APIRouter()


# By passing additional requirements to the function, we indicate that they are queries.
# By using "Optional" we communicate that they are optional values and can have a default if not passed.
# The use of Depends() allows the pydantic model to search everywhere in the request and not just in the body. This allowds the detection of variables that are in the request url
@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    report = await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    return report
