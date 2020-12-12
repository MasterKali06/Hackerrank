'''
    Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
    Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''


arr = [-4,3,-9,0,4,1]

def plusMinus(arr):
    length = len(arr)
    minus = 0
    plus = 0
    zero = 0
    for i in range(length):
        if arr[i] < 0:
            minus += 1
        elif arr[i] > 0:
            plus += 1
        else:
            zero += 1

    pos_ratio = plus/length
    neg_ratio = minus/length
    zero_ratio = zero/length

    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))


plusMinus(arr)