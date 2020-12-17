"""
    https://www.hackerrank.com/challenges/flatland-space-stations/problem

    n: the number of cities
    c: an integer array that contains the indices of cities with a space station,1-based indexing
"""


def flatlandSpaceStations(n, c):
    res = 0
    # we want to loop the stations so we sort them first
    c.sort()
    # in this method u loop to the stations and find the max distance of a city between the stations
    for i in range(1, len(c)):
        res = max(res, (c[i] - c[i - 1]) // 2)

    """
    then u find the max between the result and first station and last city minus last station
    why? because u loop through the stations not the cities .. so u need to find the distance between last city 
    and last station and first city and first station and get the max of all
    """
    res = max(res, c[0], n-1-c[-1])
    print(res)


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)