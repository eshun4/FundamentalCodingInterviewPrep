"""
Count Unique elements
"""


def count_unique_elements(lst):
    # TODO: Implement the function that counts unique elements in the given list.
    unique = list()
    seen = list()
    
    for num in lst:
        if num in unique and num not in seen:
            seen.append(num)
            unique.remove(num)
        elif num not in seen:
            unique.append(num)
    return len(unique)