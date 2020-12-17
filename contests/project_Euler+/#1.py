"""
    https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""


# this wont work in some cases ... ( time limit )
def multiple_3_5(n):
    mult = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            mult.append(i)
    print(sum(mult))


# using arithmetic progression
def multiple_3_5_(n):
    x = (n-1)//3
    y = (n-1)//5
    z = (n-1)//15
    print((x*(x+1)//2)*3 + ((y*(y+1))//2)*5 - ((z*(z+1))//2)*15)
