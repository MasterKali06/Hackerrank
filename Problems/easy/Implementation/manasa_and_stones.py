"""
    https://www.hackerrank.com/challenges/manasa-and-stones/problem

    int n: the number of non-zero stones
    int a: one possible integer difference
    int b: another possible integer difference
"""


def stones(n, a, b):
    i = 0
    stone = n
    result = []
    # stones valid cases will be --> n * a and n * b and sum of the occurence of both diff in between
    while i < stone:
        n -= 1  # we start with n - 1 because first stone is always zero
        k = (n * a) + (i * b)
        if k not in result:
            result.append(k)
        i += 1

    result.sort()
    return result
