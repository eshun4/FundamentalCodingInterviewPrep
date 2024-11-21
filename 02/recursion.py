"""
Recursion
"""


def get_sum_dp(n):
    # TODO: implement this function using recursion
    if n == 1:
        return 1
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = i + dp[i -1]
    return dp[n]


def get_sum(n):
    # TODO: implement this function using recursion
    if n == 1:
        return 1
    return n + get_sum(n - 1)

