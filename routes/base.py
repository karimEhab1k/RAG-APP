from fastapi import FastAPI , APIRouter
import os
base_router = APIRouter(
        prefix = "/api/v1",
        tags = ['api/v1']
)



@base_router.get("/")
async def welcome():
    return {
        "message":"Message From System Env",
        "APP_Name": os.getenv("APP_NAME"),
        "APP_Version": os.getenv("APP_VERSION")
    }