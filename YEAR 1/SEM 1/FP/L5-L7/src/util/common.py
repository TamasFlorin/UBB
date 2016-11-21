import datetime

class Common:
    @staticmethod
    def print_iterable(iterable:list):
        for e in iterable:
            print(e)

    @staticmethod
    def convert_to_date(arg : str):
        """Convert a string representation to a datetime.date value."""
        try:
            arg = datetime.datetime.strptime(arg,"%d.%m.%Y").date()
            return arg
        except:
            return None

    @staticmethod
    def convert_to_time(arg : str):
        """Convert a string representation to a datetime.time value."""
        try:
            arg = datetime.datetime.strptime(arg,"%H:%M").time()
            return arg
        except:
            return None
    
    @staticmethod
    def get_type(arg : str):
        """Get the data type of a string representation."""
        types = (int,float)

        for t in types:
            try:
                return type(t(arg))
            except ValueError:
                continue

        if Common.convert_to_date(arg)!=None:
            return datetime.date

        if Common.convert_to_time(arg)!=None:
            return datetime.time

        return str

    def try_convert(arg:str,arg_type):
        """Try to convert a string representation to a given type."""

        if arg_type is datetime.time and Common.get_type(arg) is datetime.time:
            return True

        if arg_type is datetime.date and Common.get_type(arg) is datetime.date:
            return True

        try:
            arg = arg_type(arg)
            return True
        except:
            return False
