from repository.repository import Repository

class FileRepository(Repository):
    def __init__(self,file_name,readEntity,writeEntity,validator_class):
        '''
        Constructor
        
        '''
        Repository.__init__(self,validator_class)
        self.__file_name = file_name
        self.__validator_class = validator_class
        self.__read_entity = readEntity
        self.__write_entity = writeEntity
        self.__readFromFile()
        
    def __readFromFile(self):
        with open(self.__file_name) as f:
            content = f.readlines()
            for line in content:
                entity = self.__read_entity(self.__file_name)
                self._entities[int(entity.entity_id)] = entity
                
    def __writeToFile(self):
        f = open(self.__file_name,'w')
        for entity in self.get_all():    
            self.__write_entity(self.__file_name,entity)
        f.close() 
    
    def save(self,entity):
        Repository.save(self, entity)
        self.__writeToFile()
        
    def remove(self,ident):
        Repository.remove(self, ident)
        self.__writeToFile()
        
    def update(self,entity):
        Repository.update(self, entity)
        self.__writeToFile()