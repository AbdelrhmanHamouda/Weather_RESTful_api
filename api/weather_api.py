from typing import Optional, List

import fastapi
from fastapi import Depends

from models.Location import Location
from models.reports import Report, ReportSubmit
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


# By passing additional requirements to the function, we indicate that they are queries.
# By using "Optional" we communicate that they are optional values and can have a default if not passed.
# The use of Depends() allows the pydantic model to search everywhere in the request and not just in the body. This allowds the detection of variables that are in the request url
@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_message, status_code=ve.status_code)
    except Exception as e:
        return fastapi.Response(content=str(e), status_code=500)


@router.get('/api/reports', name='all_reports')
async def reports_get() -> List[Report]:
    # Simulate some reporting
    # await report_service.add_report("A", Location(city="Cairo"))
    # await report_service.add_report("B", Location(city='Madrid'))
    return await report_service.get_reports()


@router.post('/api/reports', name='add_report')
async def reports_post(report_submit: ReportSubmit) -> Report:
    description = report_submit.description
    location = report_submit.location
    return await report_service.add_report(description, location)
