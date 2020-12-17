'''
    Watson likes to challenge Sherlock's math ability.
    He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints.
    Sherlock must determine the number of square integers within that range.
'''
from math import *
import timeit

# case error time limit exeed, we need to code something faster
def squares(a, b):
    count = 0
    
    for i in range(a, b+1):
        sq = sqrt(i)
        if sq.is_integer():
            count += 1
    print(count)


# faster try , timeit shows first one is faster :p
def squares1(a, b):
    count = 0
    
    sqr_list = []
    for i in range(0, 31622):
        sqr_list.append(i**2)

    for i in range(a,b+1):
        if i in sqr_list:
            count += 1

    return count

# third try, this is math so we shouldnt loop through all numbers ...
# i didnt like this one it is math not coding
def squares2(a, b):
    count = 0
    print(floor(sqrt(b)) - floor(sqrt(a - 1)))


'''
if __name__ == "__main__":

    print(timeit.timeit(stmt=test, setup="import math"))
    print(timeit.timeit(stmt=test2, setup="import math"))
'''