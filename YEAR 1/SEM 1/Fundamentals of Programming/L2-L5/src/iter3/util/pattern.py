'''
Created on 28 oct. 2016

@author: Tamas
'''
def argument_type(arg):
    """Return the type of the argument.
    
    Args:
        arg(string): the argument to check the type for.
    Returns:
        the type of the argument(int,float or str).
        
    """
    types = (int, float)
    
    for t in types:
        try:
            return type(t(arg))
        except ValueError:
            continue
        
    return str

def arguments_pattern(arguments):
    """Create a pattern based on the type of the arguments.
    Args:
        arguments(list): the list of arguments.
    Returns:
        the generated pattern.
    """
    pattern = []
    
    # reserved keywords for composite commands
    reserved_keywords = ("to", "with", ">", "<", "=", "apartment", "type")
    
    # check the type of each argument and create a pattern
    for arg in arguments:
        if arg in reserved_keywords:
            pattern.append(arg)
            continue
        
        arg_type = argument_type(arg)
        
        if arg_type == float:
            pattern.append("float")
        elif arg_type == int:
            pattern.append("int")
        else: 
            pattern.append("string")
    
    # remove the keywords from the arguments to be able to handle them
    for reserved in reserved_keywords:
        if reserved in arguments:
            arguments.remove(reserved)
    
    # return the pattern as a string
    return " ".join(pattern)