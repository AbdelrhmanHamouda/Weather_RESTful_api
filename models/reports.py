import datetime
from typing import Optional

from pydantic import BaseModel

from models.Location import Location


class Report(BaseModel):
    description: str
    location: Location
    created_date: Optional[datetime.datetime]