'''
    https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

c = [0, 0, 0, 0, 1, 0]
c1 = [0, 0, 0, 1, 0, 0]

def jumpingOnClouds(c):
    count = 0
    j = 0
    i = 0

    while j < len(c) - 3:

        if c[i + 2] == 0:
            count += 1
            j += 2
            i += 2
        else:
            count += 1
            j += 1
            i += 1
    count += 1
    print(count)

jumpingOnClouds(c)
jumpingOnClouds(c1)