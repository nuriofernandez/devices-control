# Devices Control

This is a simple API to control tuya IoT devices locally

# Endpoints (burno / opencollection)

All endpoints are available as opencollection at `bruno/`.

<img width="1230" height="576" alt="image" src="https://github.com/user-attachments/assets/b179c8e8-e9a7-4c2b-93b9-6e8cbe61ea2f" />


# Endpoints (docs / plaintext)

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

# How to run it?

First, you should make a copy of `devices.json.sample` named `devices.json`
setting your real devices settings.

```bash
cd source
cp devices.json.sample devices.json
nano devices.json
```

Second, you should make a copy of `settings.json.sample` named `settings.json`
setting there the token/password you want to use for the API authentication.

```bash
cd source
cp devices.json.sample devices.json
nano devices.json
```

Once the above is done, just execute `main.py` (located at `source/`) or use your favorite IDE.
```bash
cd source
python main.py
```
