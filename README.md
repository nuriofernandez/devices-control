# Devices Control

This is a simple API to control tuya IoT devices locally

# Endpoints

> GET /

Response:
```json
[
  {
    "name": "Office door",
    "id": "xxxxxxxxxxxxxxxxxxxxxxx"
  },
  {
    "name": "Desktop spotlight",
    "id": "xxxxxxxxxxxxxxxxxxxxxxx"
  }
]
```

> GET /{device_id}

Obtains current DPS from the device.

Response:
```json
{
  "dps": {
    "20": false,
    "21": "white",
    "22": 80,
    "23": 0,
    "24": "0000000002bc",
    "25": "06464601000003e803e800000000464601007803e803e80000000046460100f003e803e800000000",
    "26": 0,
    "34": false,
    "41": true
  }
}
```

> POST /{device_id}/on

Turns device on and retrieves device DPS status (post action)

Response:
```json
{
  "dps": {
    "20": false,
    "21": "white",
    "22": 80,
    "23": 0,
    "24": "0000000002bc",
    "25": "06464601000003e803e800000000464601007803e803e80000000046460100f003e803e800000000",
    "26": 0,
    "34": false,
    "41": true
  }
}
```

> POST /{device_id}/off

Turns device off and retrieves device DPS status (post action)

Response:
```json
{
  "dps": {
    "20": false,
    "21": "white",
    "22": 80,
    "23": 0,
    "24": "0000000002bc",
    "25": "06464601000003e803e800000000464601007803e803e80000000046460100f003e803e800000000",
    "26": 0,
    "34": false,
    "41": true
  }
}
```
