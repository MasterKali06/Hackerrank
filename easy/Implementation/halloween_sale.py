"""
    https://www.hackerrank.com/challenges/halloween-sale/problem

    int p: the price of the first game
    int d: the discount from the previous game price
    int m: the minimum cost of a game
    int s: the starting budget
"""


def howManyGames(p, d, m, s):

    count = 0

    while s >= m and s >= p:
        if p <= m:
            s = s - m
            count += 1
        else:
            s = s - p
            p = p - d
            count += 1

    return count



