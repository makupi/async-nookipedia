class CachedObject:
    def __init__(self, data: dict):
        self.updated = data.get("updated")
        self.cached = data.get("cached")
        self.api_expire_cache = data.get("api-expire-cache")
