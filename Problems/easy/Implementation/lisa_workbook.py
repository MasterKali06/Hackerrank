"""
    https://www.hackerrank.com/challenges/lisa-workbook/problem

    n: an integer that denotes the number of chapters
    k: an integer that denotes the maximum number of problems per page
    arr: an array of integers that denote the number of problems in each chapter
"""


def workbook(n, k, arr):
    page = 1
    special = 0

    for probs in arr:
        # for loop in range of 1 to probs inclusive
        for index in range(1, probs+1):
            if index == page:
                special += 1

            # condition for going to next page .. if prob ends or if the prob reaches k
            if index == probs or index % k == 0:
                page += 1

    return special
