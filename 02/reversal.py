"""
Reverse the list
"""

def solution(numbers):
    # TODO: Implement the function that reverses a list of numbers.
    reverse = []
    
    for i in range(len(numbers)-1, -1, -1):
        reverse.append(numbers[i])
    return reverse