from util.Heap import Heap
from  util.Heap import Item

class LFUCacheException(Exception):
    pass

class KeyNotFoundException(LFUCacheException):
    pass

class LFUCache(object):
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__items = Heap()

    @property
    def capacity(self):
        return self.__capacity

    def __remove_items(self):
        """ When the cache is full,remove half of the items."""
        items = [ ]
        to_remove = len(self.__items) // 2

        for _ in range(to_remove):
            item = self.__items.pop()
            items.append(item[Item.E_VALUE])
            print("Removing item: ",item[Item.E_KEY])
        return items

    def add(self,key,data):
        # if we have reached the maximum capacity,remove half of the items.
        if len(self.__items) == self.__capacity:
            return self.__remove_items()
        
        self.__items.put(key,data,0)

        return None

    def get(self,key):
        if not key in self.__items:
            raise KeyNotFoundException("Key not found!")

        # increase the priority
        self.__items.increase_priority(key)
        
        return self.__items.get(key)[Item.E_VALUE]

    def update(self,key,data):
        if not key in self.__items:
            raise KeyNotFoundException("Key not found!")

        item = self.__items.get(key)

        # also increase the priority for the item
        self.__items.update(key,data,item[Item.E_PRIORITY] + 1)

    def remove(self,key):
        if not key in self.__items:
            raise KeyNotFoundException("Key not found!")

        self.__items.remove(key)

    def get_all(self):
        return self.__items.get_all()

    def __contains__(self,key):
        return key in self.__items

    def __getitem__(self,key):
        return self.get(key)

    def __len__(self):
        return len(self.__items)