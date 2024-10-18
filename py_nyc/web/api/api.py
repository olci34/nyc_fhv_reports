from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Query
from starlette import status
import json
from py_nyc.web.api.schemas import ListTripSchema, LocDensitySchema, TripSchema
from py_nyc.web.external.nyc_open_data_api import get_trip_data

router = APIRouter()


@router.get("/home", response_model=LocDensitySchema)
def get_trips(date: str):
    req_date = datetime.fromisoformat(date)
    from_date = req_date - timedelta(hours=2)
    to_date = req_date + timedelta(hours=2)

    resp = get_trip_data(from_date, to_date)

    if resp.status_code == status.HTTP_200_OK:
        trip_list = json.loads(resp.content.decode("utf-8"))
        # trips: List[TripSchema] = []

        # for trip in list(trip_list):
        #     trips.append(TripSchema(
        #         driver_pay=float(trip["driver_pay"]),
        #         base_passenger_fare=float(trip["base_passenger_fare"]),
        #         trip_miles=float(trip["trip_miles"]),
        #         trip_time=int(trip["trip_time"]),
        #         request_datetime=datetime.fromisoformat(
        #             trip["request_datetime"]),
        #         pulocationid=int(trip["pulocationid"]),
        #         dolocationid=int(trip["dolocationid"])
        #     ))

        loc_density = {}

        for trip in list(trip_list):
            pulocationid = int(trip["pulocationid"])
            if pulocationid in loc_density:
                loc_density[pulocationid] += 1
            else:
                loc_density[pulocationid] = 1

        sorted_density = sorted(loc_density.items(),
                                key=lambda item: item[1], reverse=True)
        return {"density": sorted_density}
    else:
        print(resp)
