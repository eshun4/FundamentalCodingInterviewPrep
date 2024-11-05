"""
Implement a function that returns the first previous prime number from a number n

"""

def previous_prime(n):
    if n <= 2:
        return None
    
    i = n - 1
    while i > 1:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            return i
        i -= 1

def main():
    n = 49
    print(previous_prime(n))

if __name__ == "__main__":
    main()