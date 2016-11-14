'''
Created on 29 oct. 2016

@author: Tamas
'''
from iter3.ui.base import register_commands, \
    get_arg_names, get_function, get_pattern, ui_help
from iter3.util.pattern import arguments_pattern

def read_option():
    while True:
        try:
            option = int(input("option:"))
            return option
        except:
            print("Invalid option provided.")

def parse_arg_names(arg_names):
    """ Parse the command argument names
    Args:
        arg_names: the argument names.
    Returns:
        the parsed argument names.
    """
    arg_names = arg_names.split()
    arg_names = list(filter(lambda x: x not in("with","to",">","<","=","apartment","type"),arg_names))
    return arg_names

def read_command_input(command):
    """ Read the command input based on it's pattern.
    Args:
        command: the dictionary containing the command data.
    Returns:
        args: the list of arguments.
    Raises:
        ValueError: if the input is invalid.
    """
    arg_names = parse_arg_names(get_arg_names(command)) 

    args = []
    
    if len(get_pattern(command))==0:
        return args
    
    for arg_name in arg_names:
        args.append(input(arg_name+":"))
    
    if arguments_pattern(args)!=get_pattern(command) and get_pattern(command)!="type" and get_pattern(command)!="apartment":
        raise ValueError("Invalid input,expected: %s" % get_pattern(command))
    
    return args
        
def execute_command(transactions,backup,command):
    """ Read input data for a given command and execute it 
    """
    args = read_command_input(command)
    
    get_function(command)(transactions,backup,*args)
    
def match_command_by_index(index):
    count = 0
    
    for _,command in sorted(register_commands().items()):
        for c in command:
            if count==index:
                return c
            count +=1
            
    raise ValueError("No function found at index %d." % index)

def get_command_index(cmd_name):
    index = 0
    for key,command in sorted(register_commands().items()):
        for _ in command:
            if key==cmd_name:
                return index
            index+=1
            
    return -1

def run_menu(transactions,backup):
    
    # print the list of the commands
    ui_help()
    
    while True:
        try:
            option = read_option()
            
            if get_command_index("quit")==option:
                break;
            execute_command(transactions,backup,match_command_by_index(option))
        except KeyError as key_error:
            print(key_error)
        except ValueError as value_error:
            print(value_error)
        except Exception as exception:
            print("An error has occurred:", exception)
    