from typing import Optional

from nookipedia.api import API
from nookipedia.models import Critter, Fossil, Villager


def is_valid(data: dict) -> bool:
    if "error" in data:
        return False
    return True


class Nookipedia:
    def __init__(self, api_key: str):
        self.api = API(api_key)

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
