from typing import List, Optional, Union

from nookipedia.api import API, CachedAPI
from nookipedia.models import Fish, Villager, Bug


def is_valid(data: Union[dict, list]) -> bool:
    if "error" in data:
        return False
    if "title" in data and data["title"] == "Resource not found.":
        return False
    if type(data) is list and len(data) == 0:
        return False
    return True


class Nookipedia:
    """Main API to be used to access the Nookipedia API.

    Args:
        api_key: API key to access the Nookipedia API.
        cached_api: Whether or not the API requests should be cached in memory.
    """

    def __init__(self, api_key: str, cached_api: bool = False):
        if cached_api:
            self.api = CachedAPI(api_key)
        else:
            self.api = API(api_key)

    async def get_villager_raw(self, name: str) -> dict:
        """
        :param name: The name of the villager to get
        """
        return await self.api.get_villager(name)

    async def get_fish_raw(self, name: str) -> dict:
        """
        :param name: The name of the critter to get
        """
        return await self.api.get_fish(name)

    async def get_bug_raw(self, name: str) -> dict:
        """
        :param name: The name of the critter to get
        """
        return await self.api.get_bug(name)

    # async def get_fossil_raw(self, name: str) -> dict:
    #     """
    #     :param name: The name of the fossil to get
    #     """
    #     return await self.api.get_fossil(name)

    # async def get_today_raw(self, date: Optional[str] = None) -> dict:
    #     """
    #     :param date: Optional, the day in strtotime format (e.g. "tomororw", "+2 days")
    #     """
    #     return await self.api.get_today(date)

    async def get_villager_names(self) -> List[str]:
        """
        Returns a list of all villager names.
        """
        return await self.api.get_villager_names()

    async def get_fish_names(self) -> List[str]:
        """
        Returns a list of all fish names.
        """
        return await self.api.get_fish_names()

    async def get_bug_names(self) -> List[str]:
        """
        Returns a list of all bug names.
        """
        return await self.api.get_bug_names()

    # async def get_fossil_list(self) -> List[str]:
    #     """
    #     Returns a list of all fossil names.
    #     """
    #     return await self.api.get_fossil_list()

    async def get_category(self, name: str) -> List[str]:
        """
        :param name: The name of the category to get.
        :return: A list of all names in that category.
        """
        return await self.api.get_category(name)

    async def get_villager(self, name: str) -> Optional[Villager]:
        """

        :param name: The name of the villager to get.
        :return: Villager object, None if not found.
        """
        data = await self.api.get_villager(name)
        if not is_valid(data):
            return None
        return Villager(**data[0])

    async def get_villagers(self) -> Optional[List[Villager]]:
        """

        :return: List of Villager objects, None if not found.
        """
        data = await self.api.get_villagers()
        if not is_valid(data):
            return None
        return [Villager(**d) for d in data]

    async def get_fish(self, name: str) -> Optional[Fish]:
        """

        :param name: The name of the Fish to get.
        :return: Fish object, None if not found.
        """
        data = await self.api.get_fish(name)
        if not is_valid(data):
            return None
        return Fish(**data)

    async def get_bug(self, name: str) -> Optional[Bug]:
        """

        :param name: The name of the Bug to get.
        :return: Bug object, None if not found.
        """
        data = await self.api.get_bug(name)
        if not is_valid(data):
            return None
        return Bug(**data)

    # async def get_fossil(self, name: str) -> Optional[Fossil]:
    #     """
    #
    #     :param name: The name of the fossil to get
    #     :return: Fossil object, None if not found.
    #     """
    #     data = await self.api.get_fossil(name)
    #     if not is_valid(data):
    #         return None
    #     return Fossil(**data)
