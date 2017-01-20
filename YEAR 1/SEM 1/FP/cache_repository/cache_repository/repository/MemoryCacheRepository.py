from util.LFUCache import LFUCache

class MemoryCacheRepository(object):
    def __init__(self,cache_capacity):
        self._cache_capacity = cache_capacity
        self._cache = LFUCache(cache_capacity)

    @property
    def cache_capacity(self):
        return self._cache_capacity

    def find_by_id(self,entity_id):
        if entity_id in self._cache:
            print("Returning item {0} from cache.".format(self._cache[entity_id]))
            return self._cache[entity_id]

        return None

    def save(self,entity):
        # add the entity to the cache
        return self._cache.add(entity.entity_id,entity)

    def remove(self,entity_id):
        self._cache.remove(entity_id)

    def update(self,entity):
        self._cache.update(entity.entity_id,entity)

    def get_all(self):
        for item in self._cache.get_all():
            yield item

    def __len__(self):
        return len(self._cache)