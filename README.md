<h1 align="center">Jellyfin SDK for Python</h1>

---

<p align="center">
<img alt="Logo Banner" src="https://raw.githubusercontent.com/jellyfin/jellyfin-ux/master/branding/SVG/banner-logo-solid.svg?sanitize=true"/>
</p>

A High-level Wrapper for OpenAPI Generated Bindings for Jellyfin API.

> Warning: API changes will occur only in the final classes, bindings and legacy don't change

The main goal of this project is to be a wrapper for the API but with high level of abstraction using the power of [OpenAPI Specs bindings](https://github.com/OpenAPITools/openapi-generator) and good patterns such as [Inversion of Control](https://en.wikipedia.org/wiki/Inversion_of_control), [Method Chaining](https://en.wikipedia.org/wiki/Method_chaining), [JSONPath](https://en.wikipedia.org/wiki/JSONPath), and more.

Main unique features:
- Enables targeting a specific Jellyfin server version to ensure compatibility and prevent breaking changes.
- Supports accessing multiple servers, each potentially running different Jellyfin versions.
- Allows reducing the level of abstraction to access advanced or unavailable options through lower-level interfaces.
- Works like [AWS CDK Constructs Level](https://blog.shikisoft.com/aws-cdk-construct-levels/), more abstraction, more simple.

<div align="center">
<img width="682" height="762" alt="image" src="https://github.com/user-attachments/assets/5e878d51-6c0f-441b-a35b-94e93d9c3340" />


<em><small>How modules work together</small></em>
</div>

<small>
There is a thin layer that builds the high-level abstraction (green box/jellyfin) consuming only the bindings that already contain dataclasses and api built using the OpenAPI Generator (blue box/generated), which in turn also allows use only if the user requests jellyfin_apiclient_python (purple box/legacy) to allow for refactoring and incremental development. Both legacy and generated have classes that allow low-level access, being practically just an envelope method for requests that must communicate with the actual jellyfin API (lilac box).
</small>

This project is mainly inspired by good python library like these:
- [tmdbsimple](https://github.com/celiao/tmdbsimple)
- [plexapi](https://github.com/pushingkarmaorg/python-plexapi)
- [tensorflow](https://github.com/tensorflow/tensorflow)

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
pip install jellyfin-sdk[legacy]
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

```python
import os

os.environ["URL"] = "https://jellyfin.example.com"
os.environ["API_KEY"] = "MY_TOKEN"
```

#### Using SDK

```python
import jellyfin

api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

print(
    api.system.info.version,
    api.system.info.server_name
)
```

#### Direct with Generated Bindings

```python
from jellyfin.generated.api_10_10 import Configuration, ApiClient, SystemApi

configuration = Configuration(
    host = os.getenv("URL"),
    api_key={'CustomAuthentication': f'Token="{os.getenv("API_KEY")}"'}, 
    api_key_prefix={'CustomAuthentication': 'MediaBrowser'}
)

client = ApiClient(configuration)
system = SystemApi(client)

print(
    system.get_system_info().version, 
    system.get_system_info().server_name
)
```

#### Legacy

```python
from jellyfin.legacy import JellyfinClient
client = JellyfinClient()
client.authenticate(
    {"Servers": [{
        "AccessToken": os.getenv("API_KEY"), 
        "address": os.getenv("URL")
    }]}, 
    discover=False
)
system_info = client.jellyfin.get_system_info()

print(
    system_info.get("Version"), 
    system_info.get("ServerName")
)
```

### Jellyfin Server API Version

This is important because when a new API version is released, breaking changes can affect the entire project. 
To avoid this, you can set an API target version, similar to how it's done in Android development:

```python
from jellyfin.api import Version
import jellyfin

# By default will use the lastest stable
jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

# now let's test the new API (version 10.11) for breaking changes in same endpoint
jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY"), 
    Version.V10_11
)

# but str is allow to: 10.10, 10.11 and etc
jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY"), 
    '10.11'
)

# let's test a wrong version
jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY"), 
    '99'
)

> ValueError: Unsupported version: 99. Supported versions are: ['10.10', '10.11']
```

### List all libraries of an user

When using `API_KEY` some endpoints need the user_id (don't me ask why!), almost all issues with jellyfin is around this.
To help to identify this not-so-much-edge-cases we raise a exception to help with that:

```python

api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

api.users.libraries

> ValueError: User ID is not set. Use the 'of(user_id)' method to set the user context.


api.users.of('f674245b84ea4d3ea9cf11').libraries

# works also with the user name
api.users.of('niels').libraries

# when using 'of' the attribute of dataclasses
# user and user_view can be accessed directly
api.users.of('niels').id
```

### List all items

Item can be any object in the server, in fact that's how works, one huge table recursive linked.

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

api.items.all

# Same command but without shorthand
search = api.items.search
search

<ItemSearch (no filters set)>

search.paginate(1000)

<ItemSearch filters={
  start_index=0,
  limit=1000,
  enable_total_record_count=True
}>

search.recursive()

<ItemSearch filters={
  start_index=0,
  limit=1000,
  enable_total_record_count=True,
  recursive=True
}>
```

All filter options is available [here](https://webysther.github.io/jellyfin-sdk-python.github.io/api_10_10/docs/ItemsApi/#get_items).

The pagination uses a Iterator:

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

for item in api.items.search.paginate(100).recursive().all:
    print(item.name)
```

### Let's get the User ID by name or ID

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

uuid = api.user.by_name('joshua').id

api.user.by_id(uuid).name
```

### Get item by ID

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

api.items.by_id('ID')
```

This is just a shorthand for:

```python
api.items.search.add('ids', ['ID']).all.first
```

### Upload a Primary Image for a Item

```python
import jellyfin
from jellyfin.generated import ImageType

api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

api.image.upload_from_url(
    'ID', 
    ImageType.PRIMARY,
    'https://upload.wikimedia.org/wikipedia/commons/6/6a/Jellyfin_v10.6.0_movie_detail%2C_web_client.png'
)
```

### Add tags in a collection

Edit item require the `user_id`, but we make this easy:

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)

item = api.items.edit('ID', 'joshua')
item.tags = ['branding']
item.save()

item = api.items.edit('ID', 'niels')
item.tags = ['rules']
item.save()
```

If you want to set a global user:

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)
api.user = 'niels'

item = api.items.edit('ID')
item.tags = ['branding']
item.save()

item = api.items.edit('OTHER_ID')
item.tags = ['rules']
item.save()
```

The user on edit method has precedence over global

### Register as a client

If necessary register a client to identify ourselves to the server

```python
api = jellyfin.api(
    os.getenv("URL"), 
    os.getenv("API_KEY")
)
api.register_client()

<Api
 url='https://jellyfin.example.com',
 version='10.10',
 auth='Token="***",
       Client="4b8caf670ca1",
       Device="Linux Ubuntu 24.04.3 LTS (noble)",
       DeviceId="a7-17-23-d8-b9-b8",
       Version="24.04.3"'
>
```

If you need customize the client information:

```python
api.register_client('test')

<Api
 url='https://jellyfin.example.com',
 version='10.10',
 auth='Token="***",
       Client="test",
       Device="Linux Ubuntu 24.04.3 LTS (noble)",
       DeviceId="a7-17-23-d8-b9-b8",
       Version="24.04.3"'
>
```

For more detail look the [docs](https://webysther.github.io/jellyfin-sdk-python.github.io/sdk/#register_client).

### Documentation

- [SDK Reference](https://webysther.github.io/jellyfin-sdk-python.github.io/sdk/)
- [Jellyfin API 10.10](https://webysther.github.io/jellyfin-sdk-python.github.io/api_10_10/) (Stable)
- [Jellyfin API 10.11](https://webysther.github.io/jellyfin-sdk-python.github.io/api_10_11/) (Release Candidate)

### Supported Jellyfin Versions

| SDK Version | Jellyfin API Target |
|:-:|:-:|
| 0.1.x | 10.10.x-10.11.x |
