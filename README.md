<h1 align="center">jellyfin-sdk-python</h1>

---

<p align="center">
<img alt="Logo Banner" src="https://raw.githubusercontent.com/jellyfin/jellyfin-ux/master/branding/SVG/banner-logo-solid.svg?sanitize=true"/>
</p>

A [Possible Official](https://jellyfin.org/docs/general/contributing/branding) Python SDK for Jellyfin.

> Warning: This project is under active development, so API changes may occur.


This project is mainly inspired by good python library like these:
- [tmdbsimple](https://github.com/celiao/tmdbsimple)
- [plexapi](https://github.com/pushingkarmaorg/python-plexapi)
- [tensorflow](https://github.com/tensorflow/tensorflow)

Main unique features:
- Enables targeting a specific Jellyfin server version to ensure compatibility and prevent breaking changes.
- Supports accessing multiple servers, each potentially running different Jellyfin versions.
- Allows reducing the level of abstraction to access advanced or unavailable options through lower-level interfaces.
- Works like [AWS CDK Constructs Level](https://blog.shikisoft.com/aws-cdk-construct-levels/), more abstraction, more simple.

## Install

```sh
pip install jellyfin-sdk
```

or

```sh
uv add jellyfin-sdk
```

## Usage

### Drop-in replacement for [jellyfin-apiclient-python](https://github.com/jellyfin/jellyfin-apiclient-python)

This library includes the old legacy client (which is almost unmaintained) to help with migration:

```sh
pip uninstall jellyfin-apiclient-python
pip install jellyfin-sdk
```

```python
# change from
from jellyfin_apiclient_python import JellyfinClient
from jellyfin_apiclient_python.api import API

# to this
from jellyfin.legacy import JellyfinClient
from jellyfin.legacy.api import API
```

### Login

To get started with login, in most cases you only need to do something simple:

```python
import os

os.environ["JELLYFIN_URL"] = "https://jellyfin.example.com"
os.environ["JELLYFIN_API_KEY"] = "MY_TOKEN"
```

#### Lean optimized access

```python
import jellyfin

api = jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"))

print(api.system.info.version, api.system.info.server_name)
```

#### Generated Binding with OpenAPI Specification

```python
from jellyfin.generated.api_10_10 import Configuration, ApiClient, SystemApi

client = ApiClient(
    Configuration(host = os.getenv("JELLYFIN_URL")), 
    header_name='X-Emby-Token', 
    header_value=os.getenv("JELLYFIN_API_KEY")
)
system_info = SystemApi(client).get_system_info()

print(system_info.version, system_info.server_name)
```

#### Legacy ([jellyfin-apiclient-python](https://github.com/jellyfin/jellyfin-apiclient-python))

```python
from jellyfin.legacy import JellyfinClient
client = JellyfinClient()
client.authenticate(
    {"Servers": [{
        "AccessToken": os.getenv("JELLYFIN_API_KEY"), 
        "address": os.getenv("JELLYFIN_URL")
    }]}, 
    discover=False
)
system_info = client.jellyfin.get_system_info()

print(system_info.get("Version"), system_info.get("ServerName"))
```

### Jellyfin Server API Version

This is important because when a new API version is released, breaking changes can affect the entire project. 
To avoid this, you can set an API target version, similar to how it's done in Android development:

```python
from jellyfin.api import Version
import jellyfin

# this will use the default which is the lastest stable
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"))

# now let's test the new API (version 10.11) for breaking changes in same endpoint
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"), Version.V10_11)

# but keep simple
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"), '10.11')

# let's test a wrong version
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY"), '99')
```

### List all libraries of an user

When using `API_KEY` some endpoints need the user_id (don't me ask why!), almost all issues with jellyfin is around this.
To help to identify this not-so-much-edge-cases we raise a exception to help with that:

```python

jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.libraries

>>> jellyfin.api('https://video.webysther.org', 'f674245b80ea4a3ea9c011e01ce73ef9').user.libraries
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/code/jellyfin-sdk-python/src/jellyfin/user.py", line 16, in libraries
    return self.views
  File "/code/jellyfin-sdk-python/src/jellyfin/user.py", line 21, in views
    raise ValueError("User ID is not set. Use the 'of(user_id)' method to set the user context.")
ValueError: User ID is not set. Use the 'of(user_id)' method to set the user context.


jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.of('asdasjdkhasdjlkasdj').libraries

# works also with the user name
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.of('niels').libraries

# don't be afraid, go crazy
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.of('niels').id
```

### List all items

Item can be any object in the server, in fact that's how works, one huge table recursive linked.

```python
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).items.all
```

We still don't give you the automatic pagination with a `Iterator`, for this cases use the `filter`.
In this example will be returned 10k items. For slice the pagination use `start_index`.

```python
jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).items.filter(limit=10000)
```

### Let's get the User ID by name or ID

The id is a `UUID` to get the str just use the attribute `hex`

```python
uuid = jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.by_name('niels').id.hex

jellyfin.api(os.getenv("JELLYFIN_URL"), os.getenv("JELLYFIN_API_KEY")).user.by_id(uuid).name
```

### Supported Jellyfin Versions

| SDK Version | Jellyfin API Target |
|:-:|:-:|
| 0.1.x | 10.10.x-10.11.x |
