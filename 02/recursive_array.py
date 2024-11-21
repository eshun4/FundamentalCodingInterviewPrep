def solution(n):
    # TODO: implement
    if n == 1:
        return [1]
    return [n] + solution(n-1)