import asyncio
import os
import timeit

from dotenv import load_dotenv
from nookipedia import Nookipedia

load_dotenv()

api_key = os.getenv("NOOKIPEDIA_API_KEY")
api = Nookipedia(api_key=api_key, cached_api=True)
loop = asyncio.get_event_loop()


def run_cached_test():
    iterations = 10
    cached = True
    setup = f"""
import asyncio, os
from nookipedia import Nookipedia
api_key = os.getenv('NOOKIPEDIA_API_KEY')
api = Nookipedia(api_key=api_key, cached_api={cached})
loop = asyncio.get_event_loop()"""

    time = timeit.timeit(
        "loop.run_until_complete(api.get_villager_raw('marshal'))",
        setup=setup,
        number=iterations,
    )
    print(
        f"{iterations} iterations of .get_villager(name): {time/iterations:.3} seconds per iteration"
    )


async def test():
    villager = await api.get_villager_raw("marshal")
    critter = await api.get_critter_raw("spider")
    fossil = await api.get_fossil_raw("amber")
    print(villager)
    print(critter)
    print(fossil)
    villager = await api.get_villager("marshal")
    critter = await api.get_critter("spider")
    fossil = await api.get_fossil("amber")
    print(villager.cached)
    print(critter.cached)
    print(fossil.cached)
    today = await api.get_today_raw("+2 days")
    print(today)


loop.run_until_complete(test())
run_cached_test()
