'''
Created on 14 nov. 2016

@author: Florin
'''

def get_type(arg):
    """Get the type of an argument.
    Args:
        arg: the argument to get the type for
    Returns:
        the type of the argument.
    """
    types = (int,float)
    
    for t in types:
        try:
            return type(t(arg))
        except:
            continue
    return str