from datetime import datetime
from typing import List
from fastapi import APIRouter, Query
from starlette import status
import json
from py_nyc.web.api.schemas import ListTripSchema, TripSchema
from py_nyc.web.external.nyc_open_data_api import get_trip_data

router = APIRouter()


@router.get("/home", response_model=ListTripSchema)
def get_trips(page: int, perPage: int):
    resp = get_trip_data(page, perPage)

    if resp.status_code == status.HTTP_200_OK:
        trip_list = json.loads(resp.content.decode("utf-8"))
        trips: List[TripSchema] = []

        for trip in list(trip_list):
            trips.append(TripSchema(
                driver_pay=float(trip["driver_pay"]),
                base_passenger_fare=float(trip['base_passenger_fare']),
                trip_miles=float(trip["trip_miles"]),
                trip_time=int(trip["trip_time"]),
                request_datetime=datetime.fromisoformat(
                    trip["request_datetime"])
            ))

        return {
            "trips": trips
        }
    else:
        print(resp)
