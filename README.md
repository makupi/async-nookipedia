# async-nookipedia
Async API wrapper for Nookipedia API utilizing the [aiohttp](https://docs.aiohttp.org/en/stable/) package.

## Installation
async-nookipedia can be installed via pip.

`pip install async-nookipedia`

## Documentation

Proper docs are coming soon!

## Usage
```python
import asyncio
from nookipedia import Nookipedia


api_key = "API_KEY"

async def main():
    api = Nookipedia(api_key=api_key, cached_api=True)
    villager = await api.get_villager('marshal')
    print(villager.name)
    critter = await api.get_critter('spider')
    print(critter.name)
    fossil = await api.get_fossil('amber')
    print(fossil.name)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# Requirements
- Python >= 3.6
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [python-dateutil](https://dateutil.readthedocs.io/en/stable/) 
- [importlib_metadata](https://importlib-metadata.readthedocs.io/en/latest/)

# Issues and Features
If you're having any issues or want additional features please create an Issue on [github](https://github.com/makupi/async-nookipedia/issues).

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A015HXK)