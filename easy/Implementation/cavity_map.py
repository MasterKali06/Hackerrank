"""
    https://www.hackerrank.com/challenges/cavity-map/problem
"""


def cavityMap(grid):
    n = len(grid)
    # we dont want the edges so -->
    for i in range(1, n - 1):   # just skip the edges for rows
        for j in range(1, n - 1):   # again skip the edges for columns
            # just make a simple filter
            num = grid[i][j]
            if num > max(grid[i-1][j], grid[i][j-1], grid[i+1][j], grid[i][j+1]):
                # changing num -> X
                garb = []
                for k in grid[i]:
                    garb.append(k)
                garb[j] = "X"
                grid[i] = "".join(garb)

    return grid


if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
