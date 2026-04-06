import json
import tinytuya
from tinytuya import OutletDevice, BulbDevice

# Load device credentials & settings from 'devices.json'
with open('devices.json', 'r') as file:
    light_devices = json.load(file)

# Map device controller to the array
for device in light_devices:
    if device["type"] == "Outlet":
        device["device"] = OutletDevice(device["id"], device["ip"], device["key"])
    if device["type"] == "RGBTWLight":
        device["device"] = tinytuya.BulbDevice(device["id"], device["ip"], device["key"])

    device["device"].set_version(device["version"])
    device["device"].set_socketPersistent(True)

# Ready!
print("Loaded all devices")

def status(device_id):
    device = next((item for item in light_devices if item["id"] == device_id), None)
    return device["device"].status()

def turnOff(device_id):
    device = next((item for item in light_devices if item["id"] == device_id), None)
    device["device"].turn_off()
    return device["device"].status()

def turnOn(device_id):
    device = next((item for item in light_devices if item["id"] == device_id), None)
    device["device"].turn_on()
    return device["device"].status()

def brightness(device_id, percent):
    device = next((item for item in light_devices if item["id"] == device_id), None)

    if device["type"] == "RGBTWLight":
        device["device"].set_white_percentage(percent, 0)

    return device["device"].status()
