"""
Find numbers that are a perfect square

"""


def is_perfect_square(n):
    # TODO: implement the function that checks if a number is a perfect square
    if n < 0:
        return False 
    if n == 0:
        return True
    for i in range(1, int(n ** 0.5) + 1):
        if (i * i) == n:
            return True
        
    return False 


def main():
    n = 9
    print(is_perfect_square(n))

if __name__ == "__main__":
    main()
    
    