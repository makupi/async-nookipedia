from datetime import datetime, timedelta
from typing import Optional

from dateutil import tz

from nookipedia.api import API

EXPIRE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _valid_cache(data: dict) -> bool:
    api_cache_expire = data.get("api-cache-expire")
    us_eastern = tz.gettz("US/Eastern")
    if api_cache_expire is None:
        # exception for /critter right now
        expire = (datetime.now() + timedelta(hours=6)).replace(tzinfo=us_eastern)
        data["api-cache-expire"] = expire.strftime(EXPIRE_FORMAT)
    else:
        expire = datetime.strptime(api_cache_expire, EXPIRE_FORMAT)
        expire = expire.replace(tzinfo=us_eastern)
    if expire > datetime.now().replace(tzinfo=tz.gettz()):
        return True
    return False


def _check_cache(name: str, cache: dict) -> Optional[dict]:
    if name in cache:
        data = cache.get(name)
        if _valid_cache(data):
            return data
    return None


class CachedAPI(API):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.villager_cache = {}
        self.fossil_cache = {}
        self.fish_cache = {}
        self.bug_cache = {}

    async def get_villager(self, name: str) -> dict:
        villager = _check_cache(name, self.villager_cache)
        if villager is None:
            villager = await self._get_villager(name)
            self.villager_cache[name] = villager
        return villager

    async def get_fish(self, name: str) -> dict:
        fish = _check_cache(name, self.fish_cache)
        if fish is None:
            fish = await self._get_fish(name)
            self.fish_cache[name] = fish
        return fish

    async def get_bug(self, name: str) -> dict:
        bug = _check_cache(name, self.bug_cache)
        if bug is None:
            bug = await self._get_bug(name)
            self.bug_cache[name] = bug
        return bug

    async def get_fossil(self, name: str) -> dict:
        fossil = _check_cache(name, self.fossil_cache)
        if fossil is None:
            fossil = await self._get_fossil(name)
            self.fossil_cache[name] = fossil
        return fossil
