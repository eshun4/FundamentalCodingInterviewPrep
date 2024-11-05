"""
Prime factors of a number

"""

def get_prime_factors(n):
    # TODO: Implement the function that returns all prime factors of n
    prime_factors = []
    
    for num in range(2, int(n ** 0.5) + 1):
        if prime(num) and n % num == 0:
            prime_factors.append(num)
            while n % num == 0:
                n //= num
            
        
    if n > 1:
        prime_factors.append(n)
    return prime_factors

    
def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    

def main():
    n = 49
    print(get_prime_factors(n))

if __name__ == "__main__":
    main()