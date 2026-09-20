class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        cache = {}

    def get(self, key: int) -> int:
        if key not in cache.keys():
            return -1
        return cache[key]

    def put(self, key: int, value: int) -> None:
        cache[key] = value
