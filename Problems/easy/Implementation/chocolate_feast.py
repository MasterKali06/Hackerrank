"""
    https://www.hackerrank.com/challenges/chocolate-feast/problem

    int n: Bobby's initial amount of money
    int c: the cost of a chocolate bar
    int m: the number of wrappers he can turn in for a free bar
"""


def chocolateFeast(n, c, m):
    count = 0
    f_wrapper = n // c
    count += f_wrapper

    # easy, making a while loop and remember to keep the unused wrappers
    while f_wrapper >= m:
        unused = f_wrapper % m
        f_wrapper = f_wrapper // m
        count += f_wrapper
        f_wrapper += unused
    return count
