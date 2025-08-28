import sys, types
import jellyfin_apiclient_python
from jellyfin_apiclient_python import *

modules_legacy = [
    'api',
    'client',
    'configuration',
    'connection_manager',
    'constants',
    'credentials',
    'exceptions',
    'http',
    'keepalive',
    'timesync_manager',
    'ws_client'
]

for module_name in modules_legacy:
    if not hasattr(jellyfin_apiclient_python, module_name):
        continue
    api_module = types.ModuleType(f"jellyfin.legacy.{module_name}")
    module = getattr(jellyfin_apiclient_python, module_name)
    for attr in dir(module):
        if not attr.startswith("_"):
            setattr(api_module, attr, getattr(module, attr))
    sys.modules[f"jellyfin.legacy.{module_name}"] = api_module
