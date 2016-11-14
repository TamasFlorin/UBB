'''
Created on 27 oct. 2016

@author: Tamas
'''
from iter3.ui.base import register_commands, get_pattern, get_function
from iter3.util.pattern import arguments_pattern


def match_command_to_function(command_name, pattern):
    """Find the function that matches a given pattern.
    
    Args:
        command_name(str): the name of the command to check patterns for.
        pattern(str): the pattern to check against.
    Returns:
        the function that matches the given pattern.
    Raises:
        KeyError: if the given command name does not exist.
        ValueError: if the pattern does not match any function.
        
    """
    # create a dictionary with all the available commands stored as ( {function,pattern} }
    commands = register_commands()

    # if the command name does not exist raise an exception
    if command_name not in commands:
        raise KeyError("Command %s is not implemented." % command_name)
    
    # check if any command pattern matches our pattern
    for c in commands[command_name]:
        if pattern == get_pattern(c):
            return get_function(c)
    
    expected = ','.join([get_pattern(c) for c in commands[command_name]])
    
    # no matching pattern was found,raise an exception
    raise ValueError("Invalid syntax for command '%s' (%s), expected: (%s)" % (command_name, pattern, expected))
    
def read_command():
    """Read the command from the standard input and return it's name and arguments.
    Args:
        None
    Returns:
        cmd_name(str): the command name.
        args(list): the command arguments.
    Raises:
        ValueError : if the command is empty.
    """
    command = input("command:")
    command = command.split()
    
    if len(command) == 0:
        raise ValueError("Empty command provided.")
    
    cmd_name = command[0]
    args = command[1:]
    
    return cmd_name, args
    
def run_console(transactions,backup):
    while True:
        try:
            cmd, args = read_command()
            
            cmd = cmd.lower()
            
            if cmd in ("exit", "e", "quit", "q"):
                break;
            
            # try to find a command that matches the given arguments and execute it
            match_command_to_function(cmd, arguments_pattern(args))(transactions,backup, *args)
        
        except KeyError as key_error:
            print(key_error)
        except ValueError as value_error:
            print(value_error)
        except Exception as exception:
            print("An error has occurred:", exception)