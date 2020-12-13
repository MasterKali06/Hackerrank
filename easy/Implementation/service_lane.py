"""
    https://www.hackerrank.com/challenges/service-lane/problem
    int n: the size of the width array
    int cases[t][2]: each element contains the starting and ending indices for a segment to consider, inclusive
"""


def serviceLane(n, cases):

    result = []
    for i in cases:
        result.append(min(width[i[0]:i[1]]))

    return result
