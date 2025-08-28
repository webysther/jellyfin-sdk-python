

class System:
    def __init__(self, system_api):
        self.system_api = system_api

    @property
    def info(self):
        return self.system_api.get_system_info()