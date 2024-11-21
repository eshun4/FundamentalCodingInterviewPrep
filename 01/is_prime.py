
def is_prime_brute(n):
    """
    This is the brute force method to find the prime number
    1. It is not efficient because it iterates through all the numbes from 2 to n - 1 which is expensive.
    2. Time complexity: O(n)
    """
    
    if n <= 1:
        return False
    for i in range( 2, n -1):
        if n % i == 0:
            return False
    return True



def is_prime_optimized(n):
    """
    This is an optimized method to find the prime number
    1. It is  efficient because it iterates through all the numbes from 2 to the square root of n which is not expensive.
    2. Time complexity: O(sqrt(n))
    """
    
    if n <= 1:
        return False
    for i in range( 2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True






def main():
    n = 79
    print(is_prime_brute(n))
    print("-------------------")
    print(is_prime_optimized(n))
    

if __name__ == "__main__":
    main()
                        