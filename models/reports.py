import datetime
from typing import Optional

from pydantic import BaseModel

from models.Location import Location


class ReportSubmit(BaseModel):
    description: str
    location: Location


class Report(ReportSubmit):
    id: str
    created_date: Optional[datetime.datetime]
