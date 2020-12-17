"""
    https://www.hackerrank.com/challenges/minimum-distances/problem

    int a[n]: an array of integers
"""
from collections import Counter


def minimumDistances(a):
    counter = Counter(a)

    # listing pair numbers
    pairs = []
    for i, j in counter.items():
        if j > 1:
            pairs.append(i)

    # finding the indexes of the pairs
    distance = []
    for x in pairs:
        # this oneliner will list the index of the pairs
        indice = [i for i, val in enumerate(a) if val == x]
        distance.append(indice[1] - indice[0])

    if len(distance) > 0:
        return min(distance)
    else:
        return -1
