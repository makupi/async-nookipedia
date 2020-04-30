from .cached_object import CachedObject


class Fossil(CachedObject):
    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data.get("name")
        self.image = data.get("image")
        self.scientific_name = data.get("scientific-name")
        self.sections = data.get("sections")
        self.period = data.get("period")
        self.length = data.get("length")
        self.price = data.get("price")
        self.link = data.get("link")
