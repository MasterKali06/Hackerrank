'''
    https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
    If c[i] = 0, then cloud i is a cumulus cloud.
    If c[i] = 1, then cloud i is a thunderhead.

'''

c = [0, 0, 1, 0, 0, 1, 1, 0]
c2 = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
k = 2

def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100

    i = k % n  # finding initial jump
    energy -= c[i] * 2 + 1

    while i != 0:
        i = (i+k) % n
        energy -= c[i] * 2 + 1

    print(energy)


jumpingOnClouds(c2, 3)
