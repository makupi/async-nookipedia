from .cached_object import CachedObject


class Critter(CachedObject):
    """
    Object representing a Critter.

    :param data: JSON from API endpoint as dict.

    :var self.name: name of the critter
    :var self.image: url to the image of the critter
    :var self.scientific_name:
    :var self.family:
    :var self.time_year:
    :var self.time_day:
    :var self.location:
    :var self.size:
    :var self.rarity:
    :var self.price:
    :var self.caught:
    :var self.shadow:
    :var self.movement:
    :var self.link: url to the nookipedia page of the critter

    """

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
