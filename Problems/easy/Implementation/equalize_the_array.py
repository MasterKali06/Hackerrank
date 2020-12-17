'''
    Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.
'''
from collections import Counter

arr = [5, 3, 2, 1, 3]

def equalizeArray(arr):

    count = 0
    arr_dic = Counter(arr)
    max_count = max(arr_dic.values())
    for i, j in arr_dic.items():
        if j == max_count:
            max_num = i

    for i in arr:
        if i is not max_num:
            count += 1
    print(count)

equalizeArray(arr)