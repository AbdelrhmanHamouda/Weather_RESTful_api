from typing import Optional

from pydantic import BaseModel


# Init a pydantic model to use in the route instead of passing so many variables.
class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'US'
