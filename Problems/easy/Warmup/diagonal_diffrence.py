'''
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''

# example
vari = [[11, 2, 4,],[4, 5, 6],[10, 8, -12]]

def dD(arr):
    a = 0
    b = 0
    length = len(arr[0])
    for i in range(length):
        a += arr[i][i]
        b += arr[i][(length-i-1)]
    print(abs(a-b))

dD(vari)

