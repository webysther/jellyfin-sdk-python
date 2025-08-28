<h1 align="center">jellyfin-sdk-python</h1>

---

<p align="center">
<img alt="Logo Banner" src="https://raw.githubusercontent.com/jellyfin/jellyfin-ux/master/branding/SVG/banner-logo-solid.svg?sanitize=true"/>
</p>

A Python SDK for Jellyfin.

> Warning: This project is under active development, so API changes may occur.

## Install

```sh
pip install jellyfin-sdk
```

or

```sh
uv add jellyfin-sdk
```

## Usage

### Drop in replacement for jellyfin-apiclient-python

```python
# from
from jellyfin_apiclient_python import JellyfinClient
from jellyfin_apiclient_python.api import API

# to 
from jellyfin.legacy import JellyfinClient
from jellyfin.legacy.api import API
```

### Login

```python
import os

os.environ["JELLYFIN_URL"] = "https://jellyfin.example.com"
os.environ["JELLYFIN_API_KEY"] = "MY_TOKEN"


# legacy (jellyfin-apiclient-python)
from jellyfin.legacy import JellyfinClient
client = JellyfinClient()
client.authenticate(
    {"Servers": [{"AccessToken": os.getenv("JELLYFIN_API_KEY"), "address": os.getenv("JELLYFIN_URL")}]}, 
    discover=False
)
system_info = client.jellyfin.get_system_info()

print(system_info.get("Version"), system_info.get("ServerName"))

# generated (bindings openapi spec)
from jellyfin.generated.api_10_10 import Configuration, ApiClient, SystemApi

configuration = Configuration(host = os.getenv("JELLYFIN_URL"))
client = ApiClient(configuration, header_name='X-Emby-Token', header_value=os.getenv("JELLYFIN_API_KEY"))
system_info = SystemApi(client).get_system_info()

print(system_info.version, system_info.server_name)

# new
import jellyfin

api = jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"))

print(api.system.info.version, api.system.info.server_name)
```

### Supported Jellyfin Versions

| SDK Version | Jellyfin API Target |
|:-:|:-:|
| 0.1.0 | 10.10.x-10.11.x |