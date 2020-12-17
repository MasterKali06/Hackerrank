'''
    Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
    Using the information given below, determine the number of apples and oranges that land on Sam's house.
    s : starting point of sams house
    t : ending location of sams house
    a : location of apples tree
    b : location of oranges tree
    apples : array, location of the apples falls from the tree
    oranges : array, location of the oranges falls from the tree
'''

# test case
s = 7
t = 11
a = 5
b = 15
apple = [-2,2,1]
orange = [5,-6]


def xxx(s,t,a,b,apples,oranges):
    sams_A = 0
    sams_O = 0
    for m in range(len(apples)):
        temp = apples[m] + a
        if temp >= s and temp <= t:
            sams_A += 1


    for n in range(len(oranges)):
        temp = oranges[n] + b
        if temp >=s and temp <= t:
            sams_O += 1

    print(sams_A)
    print(sams_O)

xxx(7,11,5,15,apple,orange)
