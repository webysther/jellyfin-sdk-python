"""
Module `system` - High-level interface for SystemAPI.
"""
from __future__ import annotations

from jellyfin.generated import SystemApi, SystemInfo

class System:
    def __init__(self, api: Api):
        """Initializes the System API wrapper.

        Args:
            api (Api): An instance of the Api class.
        """
        self.system_api = api.generated.SystemApi(api.client)

    @property
    def info(self) -> SystemInfo:
        """
        Returns system information.
        
        Returns:
            SystemInfo: System information.
        """
        return self.system_api.get_system_info()