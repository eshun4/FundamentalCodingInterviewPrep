"""
You are given an integer number, 
1
≤
n
≤
1
0
6
1≤n≤10 
6
 . Your task is to write a function next_prime(n), that takes an integer n as input and returns the smallest prime number larger than n.

Here are some examples:

next_prime(7) should return 11, because 11 is the next prime number after 7.
next_prime(13) should return 17, because 17 is the next prime number after 13.
next_prime(50) should return 53, because 53 is the next prime number after 50.

"""

def next_prime(n):
    # TODO: implement the function to find the next prime number after n
    if n < 2:
        return 2
    i = n + 1
    while True:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            return i
        i += 1
            

def main():
    n = 7
    print(next_prime(n))
    
if __name__ == "__main__":
    main()
