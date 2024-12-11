"""
Find the product of all the odd digits in an integer.
"""

def solution(n):
    # TODO: implement
    product_of_odd = 1
    any_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            any_odd = True
            product_of_odd *= digit
        n = n // 10
    if not any_odd:
        return 0
    return product_of_odd