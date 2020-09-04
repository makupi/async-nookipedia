from .cached_object import CachedObject


class Bug(CachedObject):
    """
    Object representing a Bug.

    :param data: JSON from API endpoint as dict.
    :var self.url: URL to nookipedia.com entry.
    :var self.name: Name of the Bug
    :var self.image: URL to the image of the Bug.
    :var self.catchphrase:
    :var self.catchphrase2: If an additional catchphrase available, otherwise None.
    :var self.time: Time of the day as a string. e.g. "4 PM - 9 AM".
    :var self.location:
    :var self.rarity:
    :var self.sell_nook:
    :var self.sell_flick:
    :var self.tank_width:
    :var self.tank_length:
    :var self.north_months_str: Northern availability as string. e.g. "Mar – Jun; Sep – Nov"
    :var self.north_months: Array of the available months as strings.
    :var self.south_months_str: Southern availability as string. e.g. "Mar – Jun; Sep – Nov"
    :var self.south_months: Array of the available months as strings.

    """

    def __init__(self, data: dict):
        super().__init__(data)
        self.url = data.get("url")
        self.name = data.get("name")
        self.image = data.get("image")
        self.catchphrase = data.get("catchphrase")
        self.catchphrase2 = data.get("catchphrase2") or None
        self.time = data.get("time")
        self.location = data.get("location")
        self.rarity = data.get("rarity")
        self.sell_nook = data.get("sell_nook")
        self.sell_flick = data.get("sell_flick")
        self.tank_width = data.get("tank_width")
        self.tank_length = data.get("tank_length")
        self.north_months_str = data.get("n_availability")
        self.north_months = data.get("n_availability_array")
        self.south_months_str = data.get("s_availability")
        self.south_months = data.get("s_availability_array")
