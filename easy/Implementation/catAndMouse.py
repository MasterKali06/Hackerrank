'''
    https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
'''

def catAndMouse(x, y, z):
    abs1 = abs(x-z)
    abs2 = abs(y-z)
    if abs1 < abs2:
        print("Cat A")
    elif abs1 > abs2:
        print("Cat B")
    else:
        print("Mouse C")

catAndMouse(1,3,2)