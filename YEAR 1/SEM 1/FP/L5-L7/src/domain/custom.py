from enum import Enum

class IterableError(Enum):
    NOT_FOUND = -1

class Iterable:
    def __init__(self):
        self.__entities = {}
        self.__current = 0
    
    def __check_index(self,index):
        if index not in self.__entities:
            raise IndexError

    def __setitem__(self,index,value):
        self.__entities[index] = value

    def __getitem__(self,index):
        self.__check_index(index)
        return self.__entities[index]

    def values(self):
        return self.__entities.values()

    def find(self,value):
        for key,item in sorted(self.__entities.items()):
            if item == value:
                return key

        return IterableError.NOT_FOUND
    
    def __delitem__(self,index):
        self.__check_index(index)

        del self.__entities[index]

    def __next__(self):
        # set current item
        self.__current +=1

        if self.__current > len(self.__entities.items()):
            raise StopIteration

        return sorted(self.__entities.items())[self.__current-1]

    def __iter__(self):
        self.__current = 0
        return self

    def __len__(self):
        return len(self.__entities)

    def __contains__(self,value):
        return value in self.__entities

    def __str__(self):
        s = "["
        for key,item in self.__entities.items():
            s +=str(item)+ ","
        s = s[:-1]
        s+="]"
        return s

def __gnome_sort(l,upperBound,compare):
    pos = upperBound

    while pos > 0 and compare(l[pos-1],l[pos]):
        l[pos],l[pos-1] = l[pos-1],l[pos] # swap
        pos = pos - 1

def gnome_sort(l,compare = lambda x,y: x>y):
    for pos in range(1,len(l)):
        __gnome_sort(l,pos,compare)

    return l

# TODO: Implement heap sort.
def sort(l,compare = lambda x,y: x>y):
    return gnome_sort(l,compare)

def filter(func,list):
    filtered = [entity for entity in list if func(entity) ]
    return filtered