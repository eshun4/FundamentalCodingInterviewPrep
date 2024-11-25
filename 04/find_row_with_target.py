"""
You are given a matrix of integers where every row and column are sorted in ascending order. Your task is to find the row that contains a specific target value. If the target value doesn't exist, return None.

The expected time complexity is 
O(n+m)
O(n+m), where n
n is the number of rows and m
m is the number of columns.
"""

def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    # TODO: Implement the solution here
    if not matrix or not matrix[0]:
        return None
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] ==  target:
            return row
        if matrix[row][col] >  target:
            col -= 1
        if matrix[row][col] <  target:
            row += 1
    return None