import aiohttp

from nookipedia.models import Critter, Fossil, Villager

API = "https://nookipedia.com/api"


class Nookipedia:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _fetch_json(self, url: str) -> dict:
        headers = {"X-API-KEY": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()

    async def get_villager_raw(self, name: str) -> dict:
        return await self._fetch_json(f"{API}/villager/{name}/")

    async def get_critter_raw(self, name: str) -> dict:
        return await self._fetch_json(f"{API}/critter/{name}/")

    async def get_fossil_raw(self, name: str) -> dict:
        return await self._fetch_json(f"{API}/fossil/{name}/")

    async def get_villager(self, name: str) -> Villager:
        pass

    async def get_critter(self, name: str) -> Critter:
        pass

    async def get_fossil(self, name: str) -> Fossil:
        pass
