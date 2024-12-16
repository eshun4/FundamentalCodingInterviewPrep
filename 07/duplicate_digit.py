"""
Your task is to implement a function that duplicates every digit in a given non-negative integer number, n. For example, if n equals 1234, the function should return 11223344.

To prevent possible integer overflow, it is guaranteed that n will be a non-negative integer that does not exceed 
1
0
4
10 
4
 . Solve this task without converting n into a string or performing any other type of casting. Your job is to work strictly with integer operations.

Keynote:
Focus on the essence of the problem, which is processing each digit of the number independently while maintaining the digit order. There is no need to look for mathematical patterns or clever simplifications; plain and straightforward processing will suffice. Utilize the toolbox of basic programming skills: loops, conditions, and mathematical operations. Good luck!
"""

def solution(n):
    doubled_number = 0
    multiplier = 1
    
    while n > 0:
        digit = n % 10
        # Add the digit twice, each time adjusting the position with the multiplier
        doubled_number += digit * multiplier
        multiplier *= 10
        doubled_number += digit * multiplier
        multiplier *= 10
        n = n // 10
    
    return doubled_number