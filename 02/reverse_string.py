"""
Reverse String
"""


def reverse_string(s):
    # TODO: implement the function to reverse the string using recursion.
    if len(s) == 0:
        return s
    
    return s[-1] + reverse_string(s[:len(s) - 1])
        