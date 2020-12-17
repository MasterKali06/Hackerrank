"""
    https://www.hackerrank.com/challenges/the-grid-search/problem

    string G[R]: the grid to search
    string P[r]: the pattern to search for
"""

def gridSearch(G, P):



""" 
test case
1
3 3
234
111
444
2 2
23
11
"""



if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

