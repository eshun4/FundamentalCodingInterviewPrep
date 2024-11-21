"""
Continuous sub-array: Sliding window problem.
"""

def solution(listA, listB):
    # TODO: implement solution
    lenA, lenB = len(listA), len(listB)
    
    # If listB is longer than listA, it can't be a sublist
    if lenB > lenA:
        return False

    # Slide the window over listA
    for i in range(lenA - lenB + 1):
        # Use slicing to compare the segment of listA with listB
        if listA[i:i + lenB] == listB:
            return True

    return False