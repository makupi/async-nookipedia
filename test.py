import asyncio
import os
import timeit

from dotenv import load_dotenv
from nookipedia import Nookipedia

load_dotenv()

api_key = os.getenv("NOOKIPEDIA_API_KEY", "")
api = Nookipedia(api_key=api_key)
loop = asyncio.get_event_loop()


async def test():
    villager_names = await api.get_villager_names()
    villagers = await api.get_villagers()
    villager = await api.get_villager("marshal")
    bugs = await api.get_bugs()
    bug = await api.get_bug("grasshopper")
    fishes = await api.get_fishes()
    fish = await api.get_fish("sea bass")

    bug_names = await api.get_bug_names()
    fish_names = await api.get_fish_names()
    print(bug_names, fish_names)


loop.run_until_complete(test())
# run_cached_test()
