"""
Given a square matrix grid of integers, your task is to find the minimum and maximum values at the secondary diagonal. The secondary diagonal starts at the top right corner and ends at the bottom left corner.

Return a list of two elements where the first element is the minimum value, and the second is the maximum value that you have found in the diagonal. If the square matrix is empty, return [None, None].

The time complexity of the solution should not exceed 
O(n)
O(n), where n is the length of the row (or column) in the grid.
"""


def solution(grid):
    # TODO: implement the solution here
    if not grid or not grid[0]:
        return [None, None]
        
    rows, cols = len(grid), len(grid[0])
    row, col = 0, cols - 1
    mini, maxi = float('inf'), float('-inf')
    
    while row < rows and col >= 0:
        current_element = grid[row][col]
        if current_element < mini:
            mini = current_element
        if current_element > maxi:
            maxi = current_element
        row += 1
        col -= 1
    return [mini, maxi]
