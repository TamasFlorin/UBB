from domain.validators import BookException
import inspect
from util.common import Common
import collections
import datetime

class Argument(object):
    def __init__(self,name,p_type):
        self.__name = name
        self.__type = p_type

    @property
    def name(self):
        return self.__name
    
    @property
    def type(self):
        return self.__type

    def __str__(self):
        return "name: {0} type: {1}".format(self.name,self.type)

class CommandException(BookException):
    pass


class Command(object):
    """Class to allow implementation of custom commands."""
    def __init__(self,name,function,*ignore_names,arg=None):
        """Initialize the Command object.
        Args:
            name: the name of the command.
            function: the function that the command should call.
            ignore_names: the argument names that should be ignored.
            arg: an extra argument for the function(it can either be a function or any other type).
        """
        self.__name = name
        self.__function = function
        self.__arg = arg
        self.__ignore_names = ignore_names

        # the arguments for each function passed to the init method
        self.__functions_args = self.__generate__function_arguments()

    @property
    def name(self):
        return self.__name

    @property
    def arguments(self):
        return self.__functions_args

    def __get_function_args(self,function):
        """Get the arguments name and type for a function.
        Args:
            function: the function to generate the arguments for.
        Returns:
            the function arguments as a list of Argument objects.
        Raises:
            CommandException: if the 'function' argument is not a function.
        """
        if not callable(function):
            raise CommandException("Invalid function provided.")
        
        args = []

        for param in inspect.signature(function).parameters.values():
            if not param.name in self.__ignore_names:
                args.append(Argument(param.name,param.annotation))
        
        return args
    
    def __generate__function_arguments(self):
        """Generate the arguments for the 'function' and for the 'arg' if it's the case.
        Returns:
            the generated arguments for the given functions.
        """
        args = collections.OrderedDict()

        # generate arguments for the function
        args[self.__function.__name__] = self.__get_function_args(self.__function)

        # if the 'arg' is also a function generate arguments for it aswell
        if callable(self.__arg):
            args[self.__arg.__name__] = self.__get_function_args(self.__arg)

        return args

    def __prepare_function_input(self,function_args,raw_input):
        """Prepare function input based on the type of the function arguments.
        Args:
            function_args: the function arguments.
            raw_input: the input to be converted to the needed data types.
        Returns:
            the processed input.
        Raises:
            CommandException: if not enough arguments have been given.
                              if any of the arguments have an invalid type.
        """
        data = []

        # check if enough arguments have been given
        if len(function_args) !=len(raw_input):
            raise CommandException("Not enough arguments provided for the function.")

        # convert the input to the needed types
        for index,arg in enumerate(raw_input):
            if Common.try_convert(arg,function_args[index].type):
                if function_args[index].type == datetime.date:
                    data.append(Common.convert_to_date(arg))
                elif function_args[index].type == datetime.time:
                    data.append(Common.convert_to_time(arg))
                else : data.append(function_args[index].type(arg))
            else:
                raise CommandException("Invalid value given for the {0}.".format(function_args[index].name))

        return data

    def execute(self,raw_input,arg_input=None):
        """Execute the command based on the given input data.
        Args:
            raw_input: the raw input for the function.
            arg_input: the raw input for the second argument of the constructor(in case it is a function).
        Returns:
            the result of the executed function.
        """
        # prepare the input for the function
        func_args = self.__prepare_function_input(self.__functions_args[self.__function.__name__],raw_input)

        # if the second argument is also a function prepare the input(if need) for it too
        if callable(self.__arg):
            arg_input = self.__prepare_function_input(self.__functions_args[self.__arg.__name__],arg_input)
            
            if len(arg_input):
                return self.__function(self.__arg(*arg_input))
            else: 
                return self.__function(self.__arg())

        # if the second argument was given use that one
        if not self.__arg is None:
            return self.__function(self.__arg)

        # use the one passed by the user
        if len(func_args):
            return self.__function(*func_args)

        # no parameters needed
        return self.__function()



