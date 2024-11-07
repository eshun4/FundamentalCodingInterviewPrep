"""
Create a function to return the GCD of a 2 numbers
"""


def GCD(a, b): 
    if a == b: 
        return a 
    if a == 0:
        return b 
    if b == 0: 
        return a 
    if a % b == 0 or b % a == 0:
        return min(a, b) 
    a_factors = factors(a) 
    b_factors = factors(b) 
    common = set(a_factors) & set(b_factors) 
    return max(common) if common else 1
            
    
    
    
def factors(n):
    factors = []
    for i in range(1, n - 1):
        if n % i == 0:
            factors.append(i)
    return factors
    

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
        

def main():
    gcd = GCD(100, 20)
    print(gcd)

if __name__ == "__main__":
    main()