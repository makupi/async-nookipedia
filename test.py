import asyncio
import os

from dotenv import load_dotenv
from nookipedia import Nookipedia

load_dotenv()

api_key = os.getenv("NOOKIPEDIA_API_KEY")


async def test():
    api = Nookipedia(api_key=api_key)
    villager = await api.get_villager_raw("marshal")
    critter = await api.get_critter_raw("spider")
    fossil = await api.get_fossil_raw("amber")
    print(villager)
    print(critter)
    print(fossil)


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
