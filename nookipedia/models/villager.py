from .cached_object import CachedObject


class Villager(CachedObject):
    """

    :param data: JSON from API endpoint as dict.
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
