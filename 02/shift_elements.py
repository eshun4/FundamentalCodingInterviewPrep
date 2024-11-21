"""
Shift elements
"""

def shift_list_elements(ls, shift):
    # TODO: Implement the solution
    shift %= len(ls)
    return ls[-shift:] + ls[:-shift]