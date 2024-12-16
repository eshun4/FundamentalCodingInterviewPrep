"""
Your task is to construct a function that accepts an integer n and returns the integer with the same digits as n, but in reverse order. You should implement your solution using a while loop.

For instance, if the input is 12345, the output should be 54321.


Do not use built-in functions that convert the integer to another data type, such as a string, to reverse it. Solve the problem purely using mathematical operations and loop constructs.

Note that when the result has leading zeros, you should consider only the integer value (e.g., 1230 becomes 321 after the operation).
"""


def solution(n):
    # TODO: implement the solution here
    # Initialize reverse number
    reversed_number = 0
    # Iteratue until number is < 0
    while n > 0:
        # get the last digit
        last_digit = n % 10
        # Append to the end of reversed number
        reversed_number = reversed_number * 10 + last_digit
        n //= 10
    # return the number
    return reversed_number