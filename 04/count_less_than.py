"""
You're given a matrix where each row is sorted in ascending order. The columns are also sorted in ascending order. This creates a special pattern where the values in the matrix increase as you move right or down but decrease as you move left or up.

Your task is to write a Python function that counts the number of integers in the matrix that are smaller than the given target. The function should return this count as an integer.

The expected complexity is 
O(n+m)
O(n+m), where 
n
n is the number of rows and m
m is the number of columns in the matrix.

For example, given a matrix:

Copy to clipboard
[
  [1, 2, 3, 4],
  [2, 3, 4, 5],
  [3, 4, 5, 6],
  [4, 5, 6, 7]
]
and a target of 5, the function count_less_than(matrix, 5) should return 10 because there are 10 numbers in the matrix that are less than 5.

"""


def count_less_than_dfs_edition(matrix, target):
    """ This soultion is not efficient for this problem becauseit has a time complexity of O(n * m).
    This means it traverses or visits every node in the array and checks if the value at that cell is less than than
    the target. The rescursive calls can also add overhead.
    
    The most of efficient solution has a time complexity of O(n + m).
    The O(n+m) approach is more efficient because it takes advantage of the sorted properties of the matrix to minimize the number of elements you need to examine:
    Single Pass: You start from the top-right corner and make a single pass through the matrix, either moving left or down. This ensures you only traverse each row and column once.
    Direct Decisions: At each step, you make a direct decision based on the current element's comparison with the target, which reduces unnecessary checks.
    Avoids Redundancy: Unlike a DFS approach, which might revisit elements, the 
    O(n + m) method systematically narrows down the search space without revisiting elements.

This efficiency is particularly beneficial for large matrices, where reducing the number of operations can significantly improve performance. 
     
    """
    # TODO: Your code goes here. Remember that the matrix is sorted row-wise and column-wise!
    
    def dfs(matrix, row, col, visited):
        rows, cols = len(matrix), len(matrix[0])
        if row < 0 or row >= rows or col < 0 or col > cols or (row, col) in visited:
            return
        visited.add((row, col))
        directions = [(0, 1),(-1, 0)]
        for dx, dy in directions:
            new_row, new_col = col + dx, col + dy
            dfs(matrix, new_row, new_col, visited)
    # counter
    count = 0
    # visited set
    visited = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] < target:
                count += 1
                dfs(matrix, row, col, visited)
    return count
            
            
def count_less_than(matrix, target):
    # TODO: Your code goes here. Remember that the matrix is sorted row-wise and column-wise!
    """
    This is the optimized version.
    """
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    count = 0
    while row < rows and col >= 0:
        if matrix[row][col] < target:
            count += col + 1
            row += 1
        else:
            col -= 1
    return count