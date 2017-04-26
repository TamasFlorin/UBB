from repository.MemoryCacheRepository import MemoryCacheRepository
from util.LFUCache import LFUCache

class FileCacheRepositoryException(Exception):
    pass

class FileCacheRepository(MemoryCacheRepository):
    def __init__(self,cache_capacity,file_name,read_entity,write_entity):
        # initialize the base class
        super().__init__(cache_capacity)

        self.__file_name = file_name
        self.__read_entity = read_entity
        self.__write_entity = write_entity

    def __read_from_file(self,entity_id):
        """ Read an entity from file using a given function that will parse each line.
            Args:
                entity_id - the id of the entity to be read from the file.
            Returns:
                the entity matching the given id if the id exists and None otherwise.
        """
        with open(self.__file_name) as f:
            for line in f:
                entity = self.__read_entity(line)
                
                if entity.entity_id == entity_id:
                    return entity
        
        return None

    def __write_to_file(self,entity):
        """ Write an entity to the file."""
        with open(self.__file_name,"a") as f:
            line = "{0} {1}".format(self.__write_entity(entity),"\n")
            f.write(line)

    def find_by_id(self,entity_id):
        """ Find an entity that matches the given id.
            Args:
                entity_id- the id of the entity.
            Return:
                the entity matching the given id.
            Raises:
                RepositoryException - if the entity id does not exist.
        """

        # if the entity is in the cache we can return it
        entity = super().find_by_id(entity_id)

        if not entity is None:
            return entity

        # we have to read it from the file 
        entity = self.__read_from_file(entity_id)

        if entity is None:
            return None
            #raise FileCacheRepositoryException("The given entity id does not exist!")
       
        print("Returning item from file...")
       
        # add the item to the cache
        super().save(entity)

        return entity

    def save(self,entity):
        # the save method will return a list with the removed entities if the cache was full
        res = super().save(entity)

        # save the removed entities to the file
        if not res is None:
            for entity in res:
                if self.find_by_id(entity) is None: # if the entity is not present in the file
                    self.__write_to_file(entity) # save it

    def get_all(self):
        with open(self.__file_name) as f:
            for line in f:
                entity = self.__read_entity(line)
                yield entity

        return None
            


