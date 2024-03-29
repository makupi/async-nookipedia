.. async-nookipedia documentation master file, created by
   sphinx-quickstart on Fri May  1 04:16:03 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. image:: _public/Nookipedia_Leaf.png
   :width: 100
   :target: https://nookipedia.com/
   :align: right

async-nookipedia
============================================

Welcome to the async-nookipedia docs. An API wrapper for the private `Nookipedia API <https://nookipedia.com/api/>`_ for the `Nookipedia Wiki <https://nookipedia.com/>`_.    

   *async-nookipedia is not created or managed by nookipedia.*

Installation
============================================

async-nookipedia can be installed via pip as it's available on `pypi <https://pypi.org/project/async-nookipedia/>`_.

.. code-block:: guess

   pip install async-nookipedia

Basic Usage
============================================

.. code-block:: python

   import asyncio
   from nookipedia import Nookipedia


   api_key = "API_KEY"

   async def main():
       api = Nookipedia(api_key=api_key, cached_api=True)
       villager = await api.get_villager('marshal')
       print(villager.name)
       bug = await api.get_bug('spider')
       print(bug.name)
       fish = await api.get_fish('sea bass')
       print(fish.name)


   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

Caching
============================================

If **cache_api=True** is used the API requests made to nookipedia will be automatically stored in-memory until the "api-cache-expire" time is reached.    

"api-cache-require" is a timestamp for when the cache on nookipedia's end expires.



API Reference
============================================
.. toctree::
   :maxdepth: 2

   api




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Issues and Support
==================

If you're having any issues with the API wrapper open an Issue on `github <https://github.com/makupi/async-nookipedia>`_ or send me a DM on discord - maku#0001.

Donate
==================

If you like the project and think about supporting me, you can buy me a coffee on `ko-fi <https://ko-fi.com/makubob>`_. <3    


