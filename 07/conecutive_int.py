"""
You are tasked with writing a function that takes a positive integer, n, as an input and returns the number of consecutive equal digits in the number. Specifically, your function should identify pairs of digits in n that are equal and consecutive and return the count of these pairs.

For instance, if n = 113224, it contains two groups of consecutive equal digits: 11 and 22. Therefore, the output should be 2. For n = 444, the output should also be 2, as there are two groups of 44 in this number.

Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.
"""


def solution(n):
    # TODO: implement
    # Create variable to store count of consecutive digits
    consecutive_count = 0
    # Get previous digit
    prev_digit = None
    # Iterate over integer
    while n > 0:
        current_digit = n % 10
        if prev_digit == current_digit:
            consecutive_count += 1
        prev_digit = current_digit
        # Update n using integer division
        n //= 10
    return consecutive_count
        
        