from .cached_object import CachedObject


class Critter(CachedObject):
    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data.get("name")
        self.image = data.get("image")
        self.scientific_name = data.get("scientific-name")
        self.family = data.get("family")
        self.time_year = data.get("time-year")
        self.time_day = data.get("time-day")
        self.location = data.get("location")
        self.size = data.get("size")
        self.rarity = data.get("rarity")
        self.price = data.get("price")
        self.caught = data.get("caught")
        self.shadow = data.get("shadow")
        self.movement = data.get("movement")
        self.link = data.get("link")
