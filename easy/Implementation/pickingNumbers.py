'''
    https://www.hackerrank.com/challenges/picking-numbers/problem
'''


from collections import Counter
a = [3, 3, 5, 5, 2, 1, 1, 1, 4, 6, 7]

def pickingNumbers(a):

    max_num = 0
    cnt = Counter(a)
    print(cnt)
    for i in range(100):
        max_num = max(max_num, (cnt[i] + cnt[i+1]))
    print(max_num)



pickingNumbers(a)
