import enum
class StorageType(enum.Enum):
    IN_MEMORY = "inmemory"
    IN_FILE = "infile"
    IN_PICKLE_DB = "inpickledb"

class ConfigException(Exception):
    pass

class Config(object):
    def __init__(self,config_name):
        self.__config_name = config_name
        self.__storage_type = None
        self.__person_repository = None
        self.__activity_repository = None
        self.__participation_repository = None

    def parse_config(self):
        lines = []
        with open(self.__config_name) as f:
            line = f.read()

        lines = line.split("\n")

        if len(lines)<=0:
            return None

        start = lines[0].find("=")

        self.__storage_type = lines[0][start+1:].lstrip()

        if(self.__storage_type==StorageType.IN_MEMORY):
            return None

        if len(lines)<4:
            raise ConfigException("Invalid settings file provided.")

        start = lines[1].find("=")
        if start!=-1:
            self.__person_repository =  lines[1][start+1:-1].lstrip()
            self.__person_repository = self.__person_repository[1:]
           
        start = lines[2].find("=")

        if start!=-1:
            self.__activity_repository = lines[2][start+1:-1].lstrip()
            self.__activity_repository = self.__activity_repository[1:]

        start = lines[3].find("=")

        if start!=-1:
            self.__participation_repository = lines[3][start+1:-1].lstrip()
            self.__participation_repository = self.__participation_repository[1:]

    @property
    def storage_type(self):
        return self.__storage_type

    @property
    def person_repository(self):
        return self.__person_repository

    @property
    def activity_repository(self):
        return self.__activity_repository

    @property
    def participation_repository(self):
        return self.__participation_repository
