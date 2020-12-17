'''
    you have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
    If it is possible, return YES, otherwise return NO.
    x1, v1: integers, starting position and jump distance for kangaroo 1
    x2, v2: integers, starting position and jump distance for kangaroo 2
'''



def kangaroo(x1,v1,x2,v2):
    for i in range(10000):
        if ((x1 + v1) == (x2+v2)):
            print("YES")
            break
        x1+=v1
        x2+=v2
    else:
        print("NO")

kangaroo(0,3,4,2)
kangaroo(0,2,5,3)

