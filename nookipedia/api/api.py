from typing import List

import aiohttp


class API:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://nookipedia.com/api"

    async def _fetch_json(self, url: str) -> dict:
        headers = {"X-API-KEY": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()

    async def get_villager(self, name: str) -> dict:
        return await self._get_villager(name)

    async def get_critter(self, name: str) -> dict:
        return await self._get_critter(name)

    async def get_fossil(self, name: str) -> dict:
        return await self._get_fossil(name)

    async def get_today(self, date: str = "") -> dict:
        return await self._get_today(date)

    async def get_villager_list(self) -> List[str]:
        return await self._get_villager_list()

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
