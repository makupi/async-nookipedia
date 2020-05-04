from typing import List

import aiohttp


class API:
    """
    Uncached access to Nookipedia API endpoints

    :param api_key: Nookipedia API key
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://nookipedia.com/api"

    async def _fetch_json(self, url: str) -> dict:
        headers = {"X-API-KEY": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()

    async def get_villager(self, name: str) -> dict:
        """
        /villager/<name>/

        :param name: name of villager to fetch
        :return: JSON response as dict
        """
        return await self._get_villager(name)

    async def get_critter(self, name: str) -> dict:
        """
        /critter/<name>/

        :param name: name of critter to fetch
        :return: JSON response as dict
        """
        return await self._get_critter(name)

    async def get_fossil(self, name: str) -> dict:
        """
        /fossil/<name>/

        :param name: name of fossil to fetch
        :return: JSON response as dict
        """
        return await self._get_fossil(name)

    async def get_today(self, date: str = "") -> dict:
        """
        /today/<date>/

        :param date: Optional, date in strtotime format (e.g. "tomorrow", "+2 days")
        :return: JSON response as dict
        """
        return await self._get_today(date)

    async def get_villager_list(self) -> List[str]:
        """
        parses /villager/ as list of villager names

        :return: list of villager names
        """
        return await self._get_villager_list()

    async def get_critter_list(self) -> List[str]:
        """
        parses /critter/ as list of critter names

        :return: list of critter names
        """
        return await self._get_critter_list()

    async def get_fossil_list(self) -> List[str]:
        """
        parses /fossil/ as list of fossil names

        :return: list of fossil names
        """
        return await self._get_fossil_list()

    async def get_category(self, name: str) -> List[str]:
        """
        Uses the Category API endpoint to try and get a list of all names in a certain category.

        :param name: name of the category to get
        :return: list of names in that category
        """
        return await self._get_category(name)

    async def _get_villager(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/villager/{name}/")

    async def _get_critter(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/critter/{name}/")

    async def _get_fossil(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/fossil/{name}/")

    async def _get_today(self, date: str = "") -> dict:
        return await self._fetch_json(f"{self.url}/today/{date}/")

    async def _get_villager_list(self) -> List[str]:
        data = await self._fetch_json(f"{self.url}/villager/")
        villagers = list()
        for villager in data:
            name = villager.get("villager_key")
            if name is not None:
                villagers.append(name)
        return villagers

    async def _get_critter_list(self) -> List[str]:
        print(
            "ERROR get_critter_list: Unfortunately critter list is not supported by the Nookipedia API yet."
        )
        return []  # doesn't exist yet
        data = await self._fetch_json(f"{self.url}/critter/")
        critters = list()
        for critter in data:
            name = critter.get("critter_key")
            if name is not None:
                critters.append(name)
        return critters

    async def _get_fossil_list(self) -> List[str]:
        data = await self._fetch_json(f"{self.url}/fossil/")
        fossils = list()
        for fossil in data:
            name = fossil.get("fossil_key")
            if name is not None:
                fossils.append(name)
        return fossils

    async def _get_category(self, name: str) -> List[str]:
        api_url = (
            f"https://nookipedia.com/w/api.php"
            f"?action=query&list=categorymembers&cmlimit=max&format=json&cmtitle=Category:{name}"
        )
        data = await self._fetch_json(api_url)
        members = data.get("query").get("categorymembers")
        names = list()
        for member in members:
            name = member.get("title")
            names.append(name)
        return names
