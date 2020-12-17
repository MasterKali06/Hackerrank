"""
    https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""


# same time limit error in 2 cases .. we need a faster way
def even_fibo(n):
    fibo = [1, 2]
    even_fib = [2]
    for i in range(3, n):
        if i == fibo[-1] + fibo[-2]:
            fibo.append(i)
            if i % 2 == 0:
                even_fib.append(i)

    print(sum(even_fib))


# in fibo every even is 4 * lastnum + the num before
def fibo(n):
    ans = [0, 2]
    i = 2
    while i < n:
        i = (ans[-1] * 4) + ans[-2]
        ans.append(i)

    print(sum(ans[:-1]))


even_fibo(10)
fibo(600851475143)
