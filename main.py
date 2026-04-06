from fastapi import FastAPI
import uvicorn

import devices
from devices import turnOn, status, turnOff

app = FastAPI()

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