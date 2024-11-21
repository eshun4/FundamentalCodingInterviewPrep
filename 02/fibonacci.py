"""
You are given a number n. Write a function that accepts this number as an argument and utilizes recursion to find the Fibonacci number at the index n. You solution should have a complexity of 

O(n).

A Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. Thus, the sequence starts 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....

For instance, if n = 3, the function should return 2, and if n = 10, your function should return 55, which is the 10th number in the Fibonacci sequence.

Using an iterative approach to solve this problem is not allowed; you are required to solve it using recursion. Make sure to optimize your solution to have a complexity of 

O(n).
"""


def fibonacci(n: int, memo= {}) -> int:
    # TODO: implement
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]