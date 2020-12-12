'''
    You are given an array of n integers, ar = [ar[0],ar[1]...ar[n-1]] and a positive integer k.
    Find and print the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.
'''


ar = [1, 3, 2, 6, 1, 2]
k = 3
n = 6

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n):
        for j in range(0,n):
            if (((ar[i]+ ar[j])% k == 0) and i < j):
                count += 1
            j += 1
        i += 1

    print(count)

divisibleSumPairs(n,k,ar)
