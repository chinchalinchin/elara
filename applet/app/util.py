"""
util.py
-------

Static functions.
"""

def merge(d1: dict, d2: dict) -> dict:
    """
    Recursively merges two dictionaries using the union operator (|).

    :param d1: First dictionary to merge.
    :type d1: dict 
    :param d2: Second dictionary to merge.
    :type d2: dict 
    """
    if not isinstance(d1, dict):
        raise ValueError("d1 is not a dictionary!")
    
    if not isinstance(d2, dict):
        raise ValueError("d2 is not a dictionary!")

    result                  = d1 | d2

    for key in result.keys():
        if key in d1 and key in d2:
            result[key]     = merge(d1[key], d2[key])
            
    return result