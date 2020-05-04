class CachedObject:
    """
    Base Object with nookipedias caching/update parameters

    :param data: JSON from API endpoint as dict.

    :var self.updated: time when the endpoint was last updated
    :var self.cached: time when the endpoint was last cached
    :var self.api_expire_cache: time when the cache expires
    """

    def __init__(self, data: dict):
        self.updated = data.get("updated")
        self.cached = data.get("cached")
        self.api_expire_cache = data.get("api-expire-cache")
