"""
You are provided with two integers, a and b. Your task is to write a Python function that 
checks whether both a and b are co-prime or not. Two numbers are said to be co-prime or 
mutually prime if the only positive integer that divides both of them is 1. The expected complexity is 
O(sqrt(max(a,b))

For example:

Python
Copy
print(are_coprime(15, 28))   # Output: True
print(are_coprime(12, 18))   # Output: False
In the first example, the only positive integer that divides both 15 and 28 is 1; hence, they are co-prime. However, 
in the second example, 12 and 18 are divisible by 2 and 3; thus, they are not co-prime.
"""


import math

def are_coprime(a, b):
    # TODO: implement
    if math.gcd(a, b) == 1:
        return True
    return False


def main():
    a, b = 9 ,8
    print(are_coprime(a, b))
    
if __name__ == "__main__":
    main()