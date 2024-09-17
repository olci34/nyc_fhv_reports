from dotenv import load_dotenv
from py_nyc.web.api.api import router as trips_router
from fastapi import FastAPI

load_dotenv()

server = FastAPI(debug=True)

server.include_router(trips_router)
