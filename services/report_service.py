import datetime
import uuid
from typing import List

from models.Location import Location
from models.reports import Report

# This is JUST to simplify the implementation, normally, this needs to be done through a database.
__report: List[Report] = []


async def get_reports() -> List[Report]:
    # Would have an async call here
    return list(__report)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(id=str(uuid.uuid4()),
                    location=location,
                    description=description,
                    created_date=now)

    # Simulate saving to a DB.
    # Would have an async call here
    __report.append(report)
    # Sort the list to get the newest report first
    __report.sort(key=lambda r: r.created_date, reverse=True)

    return report
