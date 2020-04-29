import aiohttp

from nookipedia.models import Critter, Fossil, Villager


class Nookipedia:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _fetch_json(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"X-API-KEY": self.api_key}) as response:
                return await response.json()

    async def get_villager_raw(self, name: str) -> dict:
        pass

    async def get_critter_raw(self, name: str) -> dict:
        pass

    async def get_fossil_raw(self, name: str) -> dict:
        pass

    async def get_villager(self, name: str) -> Villager:
        pass

    async def get_critter(self, name: str) -> Critter:
        pass

    async def get_fossil(self, name: str) -> Fossil:
        pass

