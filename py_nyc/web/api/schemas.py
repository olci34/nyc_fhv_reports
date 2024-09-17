from pydantic import BaseModel
from datetime import datetime


class TripSchema(BaseModel):
    driver_pay: float
    base_passenger_fare: float
    trip_miles: float
    trip_time: int
    request_datetime: datetime


class ListTripSchema(BaseModel):
    trips: list[TripSchema]
