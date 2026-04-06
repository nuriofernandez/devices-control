import json

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn

import devices
from devices import turnOn, status, turnOff

with open('settings.json', 'r') as file:
    settings = json.load(file)

security = HTTPBearer()
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != settings["SECRET_TOKEN"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return credentials.credentials

app = FastAPI(dependencies=[Depends(verify_token)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],           # Allows all methods
    allow_headers=["*"],           # Allows all headers
)

@app.get("/")
def read_root():
    return [{"id": item["id"], "name": item["name"]} for item in devices.light_devices]

@app.get("/{item_id}")
def read_item(item_id: str, q: str = None):
    return status(item_id)

@app.post("/{item_id}/on")
def read_item(item_id: str, q: str = None):
    return turnOn(item_id)

@app.post("/{item_id}/off")
def read_item(item_id: str, q: str = None):
    return turnOff(item_id)

# Start server!
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)