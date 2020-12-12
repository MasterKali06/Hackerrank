'''
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly
    four of the five integers. Then print the respective minimum and maximum values as a single line of two
    space-separated long integers.
'''


arr = [2,1,3,4,5,6]

def mmsum(arr):
    sort_arr = sorted(arr)
    length = len(arr)
    print(str(sum(sort_arr[:(length-1)])) + ' ' + str(sum(sort_arr[1:length])))



mmsum(arr)