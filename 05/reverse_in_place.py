"""
You are given an array of n integers. Your task is to reverse the array without using any additional lists or the built-in reversed() function.

Amend the array in-place and return the array. In-place here means you are not allowed to use any additional lists in your solution.

"""

def solution(arr):
    # TODO: Implement in-place array reverse.
    left, right = 0, len(arr) -1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr