from typing import Optional

import fastapi
from fastapi import Depends

from models.Location import Location

router = fastapi.APIRouter()


# By passing additional requirements to the function, we indicate that they are queries.
# By using "Optional" we communicate that they are optional values and can have a default if not passed.
# The use of Depends() allows the pydantic model to search everywhere in the request and not just in the body. This allowds the detection of variables that are in the request url
@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    return f"{loc.city}, {loc.state}, {loc.country} in {units}"
