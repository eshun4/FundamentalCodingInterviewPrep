"""
Now, let's try to solve the same task more efficiently! We will still be searching for the longest common prefix in the given array of strings.

To add an additional layer of complexity, in this task, you need to find a more efficient approach with the expected complexity of 
O(strs.length⋅log(strs.length)⋅max_length).

Hint: think about ordering strings in some way.
"""

def efficient_LCP(strs):
    # TODO: implement the solution here
    # Sorted strings
    sorted_strs = sorted(strs)
    # First and last strings
    first, last = sorted_strs[0], sorted_strs[-1]
    # Iterate using eneumaate
    for i, char in enumerate(first):
        if char != last[i]:
            return first[:i]
    return first
    