from enum import IntEnum

class HeapException(Exception):
    pass

class KeyNotFoundException(HeapException):
    pass

class DuplicateKeyException(Exception):
    pass

class Item(IntEnum):
    E_KEY = 0
    E_VALUE = 1
    E_PRIORITY = 2 

class Heap(object):
    def __init__(self):
        self.__heap = []

        # will be used to store the position of each key in the heap
        self.__positions = {}

        self.__size = 0

    def __update_positions(self,pos1,pos2):
        """ Update the positions of two items before being swapped."""
        self.__positions[self.__heap[pos1][Item.E_KEY]] = pos2
        self.__positions[self.__heap[pos2][Item.E_KEY]] = pos1

    def __swap(self,pos1,pos2):
        """ Given two positions in the heap,swap their values."""
        self.__update_positions(pos1,pos2)
        if pos1< len(self.__heap) and pos2<len(self.__heap):
            self.__heap[pos1],self.__heap[pos2]=self.__heap[pos2],self.__heap[pos1]

    def __left_child(self,index):
        return 2*index + 1

    def __right_child(self,index):
        return 2*index + 2;

    def __parent(self,index):
        return (index-1)//2

    def __bubble_up(self,index):
        p = index
        while p > 0:
            if self.__heap[self.__parent(p)][Item.E_PRIORITY] > self.__heap[p][Item.E_PRIORITY]:
                # swap their values and update the positions
                self.__swap(self.__parent(p),p)
            else:
                # update the position of the current item
                self.__positions[self.__heap[p][Item.E_KEY]] = p
            p = self.__parent(p)

    def __sift_down(self,index):
        pass

    def put(self,key,item,priority):
        """ Put an item in the heap based on it's priority.
            Args:
                key - the unique key of the item.
                item - the item to be put in the heap.
                priority - the priority of the item.
            Raises:
                DuplicateKeyException - if the key is already present in the cache.
        """

        if key in self.__positions:
            raise DuplicateKeyException("Duplicate key!")

        # put the new entry at the end 
        self.__heap.append((key,item,priority))

        # if this is the first item,we have to set it's position
        if self.__size == 0:
            self.__positions[self.__heap[0][Item.E_KEY]] = 0
        
        # bubble up in order to keep the heap structure
        self.__bubble_up(self.__size)
        
        self.__size+=1

    def __min_heapify(self,index):
        min = index

        if self.__left_child(index) < len(self.__heap) and self.__heap[self.__left_child(index)][Item.E_PRIORITY] < self.__heap[min][Item.E_PRIORITY]:
            min = self.__left_child(index)

        if self.__right_child(index) < len(self.__heap) and self.__heap[self.__right_child(index)][Item.E_PRIORITY] < self.__heap[min][Item.E_PRIORITY]:
            min = self.__right_child(index)

        if min!=index:
            self.__swap(min,index)
            self.__min_heapify(min)

    def pop(self):
        """ Remove the item with the lowest priority and return it."""
        self.__size-=1
        self.__swap(0,self.__size)
        temp = self.__heap.pop()
        self.__min_heapify(0)

        # we no longer need the position of this item,so we can remove it
        del self.__positions[temp[Item.E_KEY]] 
        
        return temp

    def get(self,key):
        """ Return the item that has the given key.
            Args:
                key - the key of the item to be returned.
            Raises:
                KeyNotFoundException - if the key does not exist.
        """
        if not key in self.__positions:
            raise KeyNotFoundException("Key not found!")

        return self.__heap[self.__positions[key]]

    def increase_priority(self,key):
        """ Increase the priority of a given key.
            Args:
                key - the key for which to increase the priority.
        """
        current_item = self.get(key)
        self.update(key,current_item[Item.E_VALUE],current_item[Item.E_PRIORITY] + 1)

    def remove(self,key):
        """ Remove any key from the heap."""
        if not key in self.__positions:
            raise KeyNotFoundException("Key not found!")

        if(self.__size == 1):
            del self.__heap[self.__positions[key]]
            del self.__positions[key]
            self.__size = 0
            return

        self.__size -=1

        # swap the item with the last one
        self.__swap(self.__positions[key],self.__size)
        
        # remove the last item
        temp = self.__heap.pop()

        # restore the heap property
        self.__min_heapify(self.__positions[key])

        # we do not need this position anymore
        del self.__positions[temp[Item.E_KEY]]

    def update(self,key,item,priority):
        """ Update a key in the heap."""
        if not key in self.__positions:
            raise KeyNotFoundException("Key not found!")

        self.__heap[self.__positions[key]] = (key,item,priority)

        # if the new priority is smaller then we have to bubble up
        self.__bubble_up(self.__positions[key])

        # else,we have to swift down
        self.__min_heapify(self.__positions[key])

    def __len__(self):
        return self.__size

    def __contains__(self,key):
        return key in self.__positions

    def __getitem__(self,key):
        return self.__heap[self.__positions[key]]

    def __setitem__(self,key,item,priority):
        if not key in self.__positions:
            self.put(key,item,priority)
            return

        self.update(key,item,priority)

    def get_all(self):
        return sorted(self.__heap,key = lambda x: x[Item.E_PRIORITY])