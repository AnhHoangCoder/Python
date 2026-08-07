#LRU thủ công bộ đệm hệ thống

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

            self.cache[key] = value

cache = LRUCache(2)

cache.put(1, 1)
print(cache.cache)

cache.put(2, 2)
print(cache.cache)

print(cache.get(1))
print(cache.cache)

cache.put(3, 3)
print(cache.cache)

print(cache.get(2))

cache.put(4, 4)
print(cache.cache)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))