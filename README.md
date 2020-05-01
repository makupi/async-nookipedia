# async-nookipedia
Async API wrapper for Nookipedia API utilizing the [aiohttp](https://docs.aiohttp.org/en/stable/) package.

## Installation
async-nookipedia can be installed via pip.

`pip install async-nookipedia`

## Usage
```python
import asyncio
from nookipedia import Nookipedia


api_key = "API_KEY"

async def main():
    api = Nookipedia(api_key=api_key, cached_api=True)
    villager = await api.get_villager('marshal')
    print(villager.name)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

