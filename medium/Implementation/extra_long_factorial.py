'''
    Calculate and print the factorial of a given integer.
    n! = n * n-1 * n-2 .... 3 * 2 * 1
'''

def extraLongFactorials(n):

    len = n
    final_res = 0
    res = n
    if n == 1 or n == 2:
        res = n
    else:
        for i in range(len - 1):
            next_op = n - 1
            res = res * (next_op)

            n -= 1
            i += 1

    print(res)

extraLongFactorials(3)