from datetime import datetime
from typing import Optional

from dateutil import tz

from nookipedia.api import API


def valid_cache(data: dict) -> bool:
    api_cache_expire = data.get("api-cache-expire")
    expire = datetime.strptime(api_cache_expire, "%Y-%m-%d %H:%M:%S")
    us_eastern = tz.gettz("US/Eastern")
    expire = expire.replace(tzinfo=us_eastern)
    if expire > datetime.now().replace(tzinfo=tz.gettz()):
        return True
    return False


def check_cache(name: str, cache: dict) -> Optional[dict]:
    if name in cache:
        data = cache.get(name)
        if valid_cache(data):
            return data
    return None


class CachedAPI(API):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.villager_cache = {}
        self.fossil_cache = {}
        self.critter_cache = {}

    async def get_villager(self, name: str) -> dict:
        villager = check_cache(name, self.villager_cache)
        if villager is None:
            villager = await self._get_villager(name)
            self.villager_cache[name] = villager
        return villager

    async def get_critter(self, name: str) -> dict:
        critter = check_cache(name, self.critter_cache)
        if critter is None:
            critter = await self._get_critter(name)
            self.critter_cache[name] = critter
        return critter

    async def get_fossil(self, name: str) -> dict:
        fossil = check_cache(name, self.fossil_cache)
        if fossil is None:
            fossil = await self._get_fossil(name)
            self.fossil_cache[name] = fossil
        return fossil
