from .cached_object import CachedObject


class Villager(CachedObject):
    """
    Object representing a Villager.

    :param data: JSON from API endpoint as dict.

    :var self.url: url to the nookipedia page of the villager
    :var self.name:
    :var self.image: url to the image of the villager
    :var self.species:
    :var self.personality:
    :var self.gender:
    :var self.birthday:
    :var self.sign:
    :var self.quote:
    :var self.phrase:
    :var self.previous_phrases:
    :var self.clothing:
    :var self.islander: boolean whether the villager is an islander or not
    :var self.photo_url:
    :var self.icon_url:
    :var self.sub_personality:
    :var self.clothing_variant:
    :var self.favourite_styles:
    :var self.favourite_colors:
    :var self.hobby:
    :var self.house_interior_image:
    :var self.house_exterior_image:
    :var self.house_wallpaper:
    :var self.house_flooring:
    :var self.house_music:
    :var self.house_music_note:
    """

    def __init__(self, data: dict):

        super().__init__(data)
        self.url = data.get("url")
        self.name = data.get("name")
        self.image = data.get("image_url")
        self.species = data.get("species")
        self.personality = data.get("personality")
        self.gender = data.get("gender")
        self.birthday = data.get("birthday")
        self.sign = data.get("sign")
        self.quote = data.get("quote")
        self.phrase = data.get("phrase")
        self.previous_phrases = data.get("prev_phrases")
        self.clothing = data.get("clothing")
        self.islander = data.get("islander")
        nh_details = data.get("nh_details")
        self.photo_url = nh_details.get("photo_url")
        self.icon_url = nh_details.get("icon_url")
        self.sub_personality = nh_details.get("sub_personality")
        self.clothing_variant = nh_details.get("clothing_variant")
        self.favourite_styles = nh_details.get("fav_styles")
        self.favourite_colors = nh_details.get("fav_colors")
        self.hobby = nh_details.get("hobby")
        self.house_interior_image = nh_details.get("house_interior_url")
        self.house_exterior_image = nh_details.get("house_exterior_url")
        self.house_wallpaper = nh_details.get("house_wallpaper")
        self.house_flooring = nh_details.get("house_flooring")
        self.house_music = nh_details.get("house_music")
        self.house_music_note = nh_details.get("house_music_note")
