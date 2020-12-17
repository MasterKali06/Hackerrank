'''
    https://www.hackerrank.com/challenges/append-and-delete/problem

    The first line contains a string s, the initial string.
    The second line contains a string t, the desired final string.
    The third line contains an integer k, the number of operations.
'''

# some cool shit i wrote but didnt work in some scenarios
def appendAndDelete(s, t, k):

    moves = 0
    s = list(s)
    t = list(t)

    l_s = len(s)
    l_t = len(t)

    if l_s >= l_t:
        for i in range(l_t):
            if t[i] != s[i]:
                moves += 2

    else:
        for i in range(l_s):
            if t[i] != s[i]:
                moves += 2



    if moves <= k:
        print("YES")
    else:
        print("NO")

s = "hackerhappy"
t= "hackerrank"



def appendAndDelete1(s, t, k):
    count = 0
    total_len = len(s) + len(t)

    # finding the first equal chars until the one that is diffrent
    for i, j in zip(s, t):
        if i == j:
            count += 1
        else:
            break

    if ((2 * count + k) >= total_len and total_len%2 == k%2) or total_len < k:
        print("Yes")
    else:
        print("No")

