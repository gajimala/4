
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/lifesavers/gangneung")
def get_lifesavers():
    with open("gangneung_lifesavers.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
