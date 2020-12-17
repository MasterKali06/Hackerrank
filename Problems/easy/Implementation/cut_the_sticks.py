'''
    https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''

arr = [5, 4, 4, 2, 2, 8]
arr2 = [1, 2, 3, 4, 3, 3, 2, 1]

# failed // resolved it with help and it work .. had some issues
def cutTheSticks(arr):
    result = []


    while len(arr):
        result.append(len(arr))

        arr = [ i - min(arr) for i in arr]

        min_stick = min(arr)
        for j in range(arr.count(min_stick)):
            arr.remove(min_stick)


    print(result)

cutTheSticks(arr)
cutTheSticks(arr2)

# second way
def cutTheSticks1(arr):
    count = 0
    new_sticks = []

    if arr:
        small_sticks = min(arr)
    else:
        return

    for i in arr:
        count += 1
        new_el = i - small_sticks
        if new_el != 0:
            new_sticks.append(new_el)
    print(count)

    cutTheSticks1(new_sticks)

#cutTheSticks1(arr2)

# coolest way
from collections import Counter

def cutTheSticks2(arr):
    res = []
    n = len(arr)
    s = Counter(arr)
    for i in sorted(s.keys()):
        res.append(n)
        n -= s[i]
    print(res)

#cutTheSticks2(arr2)

