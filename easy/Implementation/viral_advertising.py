'''
    https://www.hackerrank.com/challenges/strange-advertising/problem
'''



def viralAdvertising(n):
    # defaults according to the problem
    liked = 0
    shared = 5
    cumulative = 0
    new_share = 0

    for i in range(0,n):
        liked = shared // 2
        shared = liked * 3
        cumulative += liked

    print(cumulative)

viralAdvertising(5)
