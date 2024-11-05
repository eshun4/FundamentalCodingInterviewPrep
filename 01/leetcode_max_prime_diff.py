"""
Leetcode maximum prime difference:
"""


def maxPrimeDiff(array):
    n = len(array)
    prime_indices = [i for i in range(n) if prime(array[i])]
    if len(prime_indices) < 2:
        return 0  # If there's only one prime number, the distance is 0
    return max(prime_indices) - min(prime_indices)


def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


    
def main():
    inp = [4, 2, 9, 5, 3]
    print(maxPrimeDiff(inp))  # Expected output: 3
    
if __name__ == "__main__":
    main()