"""
    https://www.hackerrank.com/challenges/beautiful-triplets/problem

    d: an integer
    arr: an array of integers, sorted ascending
"""

# test case
arr1 = [1, 2, 4, 5, 7, 8, 10]
d1 = 3


def beautifulTriplets(d, arr):

    count = 0

    for i in arr:
        if i + d in arr:
            if i + (2*d) in arr:
                count += 1

    print(count)


beautifulTriplets(d1, arr1)
