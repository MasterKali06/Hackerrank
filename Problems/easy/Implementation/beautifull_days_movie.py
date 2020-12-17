'''
    https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
'''

def beautifulDays(i, j, k):
    day_count = 0
    for day in range(i,j+1):
        reverse_day = int(str(day)[::-1])
        x = abs(day - reverse_day)
        if x % k == 0:
            day_count += 1
        day += 1
    print(day_count)


beautifulDays(20, 23, 6)