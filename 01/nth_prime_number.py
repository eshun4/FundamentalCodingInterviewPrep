"""
You are given a number n. Your task is to write a function that will return the n-th prime number. The expected complexity is 
O(n⋅sqrt(n))


For example, if n is 1, the function should return 2. If n is 3, the function should return the third prime number, which is 5
"""

def nth_prime(n: int) -> int:
    # TODO: implement the function
    p_numbers = []
    i = 2
    while len(p_numbers) < n:
        if prime(i):
            p_numbers.append(i)
        i += 1
    return p_numbers[n-1]


def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    
def main():
    n = 5
    print(nth_prime(n))  # Expected output: 3
    
if __name__ == "__main__":
    main()