"""
    https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
"""


def prime_factor(n):
    # largest prime is equal to num itself before we do any math and smallest prime is i = 2
    largest_prim = n
    i = 2
    while i*i <= n:
        while n % i == 0:
            largest_prim = i
            n //= i
        i += 1

    if largest_prim > n:
        largest_prim = n
    print(largest_prim)


prime_factor(17)
