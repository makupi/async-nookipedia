from .cached_object import CachedObject


class Villager(CachedObject):
    """
    Object representing a Villager.

    :param data: JSON from API endpoint as dict.

    :var self.message: message from nookipedia
    :var self.name: name of the villager
    :var self.image: url to the image of the villager
    :var self.quote:
    :var self.gender:
    :var self.personality:
    :var self.species:
    :var self.birthday:
    :var self.sign: villagers zodiac sign
    :var self.phrase:
    :var self.clothes:
    :var self.islander_favorite:
    :var self.islander_allergic:
    :var self.picture: url to an image of the villagers framed picture
    :var self.siblings:
    :var self.skill:
    :var self.goal:
    :var self.fear:
    :var self.fav_clothing:
    :var self.least_fav_clothing:
    :var self.fav_color:
    :var self.coffee_type:
    :var self.coffee_milk:
    :var self.coffee_sugar:
    :var self.link: url to the nookipedia page of the villager
    """

    def __init__(self, data: dict):

        super().__init__(data)
        self.message = data.get("message")
        self.name = data.get("name")
        self.image = data.get("image")
        self.quote = data.get("quote")
        self.gender = data.get("gender")
        self.personality = data.get("personality")
        self.species = data.get("species")
        self.birthday = data.get("birthday")
        self.sign = data.get("sign")
        self.phrase = data.get("phrase")
        self.clothes = data.get("clothes")
        self.islander_favorite = data.get("islander-favorite")
        self.islander_allergic = data.get("islander-allergic")
        self.picture = data.get("picture")
        self.siblings = data.get("siblings")
        self.skill = data.get("skill")
        self.goal = data.get("goal")
        self.fear = data.get("fear")
        self.fav_clothing = data.get("favclothing")
        self.least_fav_clothing = data.get("leastfavclothing")
        self.fav_color = data.get("favcolor")
        self.coffee_type = data.get("coffee-type")
        self.coffee_milk = data.get("coffee-milk")
        self.coffee_sugar = data.get("coffee-sugar")
        self.link = data.get("link")
