from .cached_object import CachedObject


class Fossil(CachedObject):
    """
        Object representing a Critter.

        :param data: JSON from API endpoint as dict.

        :var self.name: name of the fossil
        :var self.image: url to the image of the fossil
        :var self.scientific_name:
        :var self.sections:
        :var self.period:
        :var self.length:
        :var self.price:
        :var self.link: url to the nookipedia page of the fossil
    """

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
