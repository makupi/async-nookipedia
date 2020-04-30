from typing import List, Optional

from nookipedia.api import API, CachedAPI
from nookipedia.models import Critter, Fossil, Villager


def is_valid(data: dict) -> bool:
    if "error" in data:
        return False
    return True


class Nookipedia:
    def __init__(self, api_key: str, cached_api=False):
        if cached_api:
            self.api = CachedAPI(api_key)
        else:
            self.api = API(api_key)

    async def get_villager_raw(self, name: str) -> dict:
        return await self.api.get_villager(name)

    async def get_critter_raw(self, name: str) -> dict:
        return await self.api.get_critter(name)

    async def get_fossil_raw(self, name: str) -> dict:
        return await self.api.get_fossil(name)

    async def get_today_raw(self, date: str = "") -> dict:
        return await self.api.get_today(date)

    async def get_villager_list(self) -> List[str]:
        return await self.api.get_villager_list()

    async def get_critter_list(self) -> List[str]:
        return await self.api.get_critter_list()

    async def get_fossil_list(self) -> List[str]:
        return await self.api.get_fossil_list()

    async def get_villager(self, name: str) -> Optional[Villager]:
        data = await self.api.get_villager(name)
        if not is_valid(data):
            return None
        return Villager(data=data)

    async def get_critter(self, name: str) -> Optional[Critter]:
        data = await self.api.get_critter(name)
        if not is_valid(data):
            return None
        return Critter(data=data)

    async def get_fossil(self, name: str) -> Optional[Fossil]:
        data = await self.api.get_fossil(name)
        if not is_valid(data):
            return None
        return Fossil(data=data)
