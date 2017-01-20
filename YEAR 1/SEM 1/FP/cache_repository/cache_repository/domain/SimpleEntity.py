class SimpleEntity(object):
    def __init__(self,entity_id,name,age):
        self.__entity_id = entity_id
        self.__name = name
        self.__age = age

    @property
    def entity_id(self):
        return self.__entity_id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return "{0} {1} {2}".format(self.__entity_id,self.__name,self.__age)

def read_entity(line):
    line = line.split(" ")
    return SimpleEntity(int(line[0]),line[1],int(line[2]))

def write_entity(entity):
    line = "{0} {1} {2}".format(entity.entity_id,entity.name,entity.age)
    return line

