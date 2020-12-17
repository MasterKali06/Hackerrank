'''
    https://www.hackerrank.com/challenges/queens-attack-2/problem

    - n: an integer, the number of rows and columns in the board
    - k: an integer, the number of obstacles on the board
    - r_q: integer, the row number of the queen's position
    - c_q: integer, the column number of the queen's position
    - obstacles: a two dimensional array of integers where each element is an array of 2 integers, the row and column of an obstacle
'''



def queensAttack(n, k, r_q, c_q, obstacles):

    count = 0
    obst = []

    # listing the 8 direction
    dist = [0] * 8
    dist[0] = n-c_q                 #dist[0] + x-axis
    dist[1] = n-r_q                 #dist[1] + y-axis
    dist[2] = c_q-1                 #dist[2] - x-axis
    dist[3] = r_q-1                 #dist[3] - y-axis
    dist[4] = min(dist[0], dist[1]) #dist[4] (+ +)
    dist[5] = min(dist[2], dist[1]) #dist[5] (- +)
    dist[6] = min(dist[2], dist[3]) #dist[6] (- -)
    dist[7] = min(dist[0], dist[3]) #dist[7] (+ -)


    for ob in obstacles:
        x = ob[1]
        y = ob[0]
        xx = x - c_q
        yy = y - r_q
        if yy == 0 and x > c_q:
            if [r_q, c_q + 1] not in obst:
                obst.append([r_q, c_q + 1])
                count += x - c_q - 1

        if yy == 0 and x < c_q:
            if [r_q, c_q -1] not in obst:
                obst.append([r_q, c_q - 1])
                count += c_q - x - 1

        if xx == 0 and y > r_q:
            if [r_q+1, c_q] not in obst:
                obst.append([r_q + 1, c_q])
                count += y - r_q - 1

        if xx == 0 and y < r_q:
            if [r_q - 1, c_q] not in obst:
                obst.append([r_q - 1, c_q])
                count += r_q - y - 1

        if y - r_q == x - c_q and y>r_q and x>c_q:
            if [r_q + 1, c_q + 1] not in obst:
                obst.append([r_q+1, c_q+1])
                count += abs(y - r_q) - 1

        if y - r_q == c_q - x and c_q>x and y>r_q:
            if [r_q + 1, c_q -1] not in obst:
                obst.append([r_q+1,c_q-1])
                count += abs(x - c_q) - 1

        if r_q - y == c_q - x and r_q>y and c_q>x:
            if [r_q-1, c_q-1] not in obst:
                obst.append([r_q-1, c_q-1])
                count += abs(r_q - y) - 1

        if r_q - y == x - c_q and r_q>y and x>c_q:
            if [r_q - 1, c_q + 1] not in obst:
                obst.append([r_q-1, c_q+1])
                count += abs(y - r_q) - 1


    for i in obst:
        if i not in obstacles:
            obstacles.append(i)


    if [r_q, c_q+1] not in obstacles:
        count += dist[0]

    if [r_q + 1, c_q + 1] not in obstacles:
        count += dist[4]

    if [r_q + 1, c_q] not in obstacles:
        count += dist[1]

    if [r_q + 1, c_q - 1] not in obstacles:
        count += dist[5]

    if [r_q, c_q - 1] not in obstacles:
        count += dist[2]

    if [r_q - 1, c_q - 1] not in obstacles:
        count += dist[6]

    if [r_q -1, c_q] not in obstacles:
        count += dist[3]

    if [r_q -1, c_q + 1] not in obstacles:
        count += dist[7]

    print(count)



'''
    another way that i found in youtube ... i couldnt get the nearest obstacles and iterate correctly
    so 3 / 22 test cases were wrong with the solution top .. its faster my way but not correct in all cases
'''

def queensAttack1(n, k, r_q, c_q, obstacles):
    total = 0
    obs = {}

    for i,j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j:1}

    def limit(x, y):
        return True if 1<=x<=n and 1<=y<=n else False

    def check(x, y, xi, yi):
        count = 0
        x += xi
        y += yi
        while limit(x, y) and obs.get(x, {}).get(y, 0)==0:
            print(x , y)
            count += 1
            x += xi
            y += yi
        return count

    r = [0, 0, -1, 1, -1, 1, -1, 1]
    c = [1, -1, 0, 0, -1, 1, 1, -1]

    for i, j in zip(r, c):
        total += check(r_q, c_q, i, j)

    print(total)

if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)