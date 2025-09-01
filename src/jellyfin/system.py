"""
Module `system` - High-level interface for SystemAPI.
"""

class System:
    def __init__(self, system_api: object):
        """Initializes the System API wrapper.

        Args:
            system_api (SystemApi): An instance of the generated SystemApi class.
        """
        self.system_api = system_api

    @property
    def info(self):
        """
        Returns system information.
        
        Returns:
            SystemInfo: System information.
        """
        return self.system_api.get_system_info()