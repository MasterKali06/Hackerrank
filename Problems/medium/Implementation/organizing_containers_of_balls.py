'''
    https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
'''

import pandas as pd
# easy solve with pandas
def organizingContainers(container):

    p = pd.DataFrame(container)
    if p.sum(axis=0).equals(p.sum(axis=1)):
        print("Possible")
    else:
        print("Impossible")


# normal way
def organizingcontainers(container):
    row_sum = [sum(x) for x in container]
    col_sum = [sum(x) for x in zip(*container)]

    if sorted(row_sum) == sorted(col_sum):
        print("Possible")
    else:
        print("Impossible")

if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingcontainers(container)