"""
    https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem
"""


def palindrome(n):
    large = 0
    i = 101101
    while i <= n:
        i = str(i)
        if i == i[::-1]:
            large = int(i)
        i = int(i)
        i += 1

    print(int(large))


palindrome(101110)