

class Items:
    def __init__(self, items_api):
        self.items_api = items_api
        
    @property
    def all(self):
        return self.filter()

    @property
    def filter(self):
        return self.items_api.get_items