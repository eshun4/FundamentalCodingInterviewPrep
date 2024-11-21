def solution(lst, val):
    # TODO: Implement the function
    for i in range(0, len(lst)):
        if lst[i] == val:
            return i
    return -1
    