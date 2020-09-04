import logging
from typing import List, Union

import aiohttp


SUPPORTED_API_VERSION = "1.0.0"


class API:
    """
    Uncached access to Nookipedia API endpoints

    :param api_key: Nookipedia API key
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.nookipedia.com/"

    async def _fetch_json(self, url: str) -> Union[List[str], List[dict], dict]:
        headers = {"X-API-KEY": self.api_key, "Accept-Version": SUPPORTED_API_VERSION}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()

    async def get_villagers(self) -> List[dict]:
        """
        GET /villagers

        :return: List of villagers as dict
        """
        return await self._get_villagers()

    async def get_villager(self, name: str) -> dict:
        """
        GET /villagers?name=name

        :param name: name of villager to fetch
        :return: JSON response as dict
        """
        return await self._get_villager(name)

    async def get_fish(self, name: str) -> dict:
        """
        GET /nh/fish/<name>

        :param name: name of new horizon fish to fetch
        :return: JSON response as dict
        """
        return await self._get_fish(name)

    async def get_bug(self, name: str) -> dict:
        """
        GET /nh/bug/<name>

        :param name: name of new horizon bug to fetch
        :return: JSON response as dict
        """
        return await self._get_bug(name)

    async def get_fossil(self, name: str) -> dict:
        """
        /fossil/<name>/
        NOT YET SUPPORTED BY NEW API.
        :param name: name of fossil to fetch
        :return: JSON response as dict
        """
        return await self._get_fossil(name)

    async def get_today(self, date: str = "") -> dict:
        """
        /today/<date>/
        NOT YET SUPPORTED BY NEW API.
        :param date: Optional, date in strtotime format (e.g. "tomorrow", "+2 days")
        :return: JSON response as dict
        """
        return await self._get_today(date)

    async def get_villager_names(self) -> List[str]:
        """
        GET /villagers?excludedetails=true to return list of villager names

        :return: list of villager names
        """
        return await self._get_villager_list()

    async def get_fish_names(self) -> List[str]:
        """
        GET /nh/fish?excludedetails=true to return a list of fish names

        :return: list of critter names
        """
        return await self._get_fish_names()

    async def get_bug_names(self) -> List[str]:
        """
        GET /nh/bug?excludedetails=true to return a list of bug names

        :return: list of critter names
        """
        return await self._get_bug_names()

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

    async def _get_villagers(self) -> List[dict]:
        return await self._fetch_json(f"{self.url}/villagers&game=NH")

    async def _get_villager(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/villagers&game=NH?name={name}/")

    async def _get_fish(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/nh/fish/{name}")

    async def _get_bug(self, name: str) -> dict:
        return await self._fetch_json(f"{self.url}/nh/bug/{name}")

    async def _get_fossil(self, name: str) -> dict:
        logging.error("/fossil is not yet supported by the new nookipedia API.")
        return {}
        return await self._fetch_json(f"{self.url}/fossil/{name}/")

    async def _get_today(self, date: str = "") -> dict:
        logging.error("/today is not yet supported by the new nookipedia API.")
        return {}
        return await self._fetch_json(f"{self.url}/today/{date}/")

    async def _get_villager_names(self) -> List[str]:
        data = await self._fetch_json(
            f"{self.url}/villagers?game=NH&excludedetails=true"
        )
        return data

    async def _get_fish_names(self) -> List[str]:
        data = await self._fetch_json(f"{self.url}/nh/fish?excludedetails=true")
        return data

    async def _get_bug_names(self) -> List[str]:
        data = await self._fetch_json(f"{self.url}/nh/bug?excludedetails=true")
        return data

    async def _get_fossil_list(self) -> List[str]:
        logging.error("/fossil/ is not yet supported by the new nookipedia API.")
        return []
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
