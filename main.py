from fastapi import FastAPI
from dotenv import load_dotenv
import os

from api.router import router

load_dotenv()
API_SECRET = os.getenv("API_SECRET_KEY")

app = FastAPI(title="Bom Mar SC API")


app.include_router(router)
