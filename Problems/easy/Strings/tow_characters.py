"""
    https://www.hackerrank.com/challenges/two-characters/problem
"""
from itertools import combinations


def alternate(s):
    # first we make a list of uniq characters
    uniq = []
    for i in s:
        if i not in uniq:
            uniq.append(i)

    valid_cases = []    # a list for adding the valid cases
    # combination will make a list of uniq chars in pairs (ex --> (a , b) ... )
    for i in combinations(uniq, 2):
        res = []
        # logic is we loop in string chars and will test uniq pairs consequence and capture the valid ones
        for char in s:
            # char must be in uniq pairs
            if (char in i and len(res) == 0) or char in i:
                # condition: if the char is same as last one ( invalid ) we break
                if len(res) >= 1 and char == res[-1]:
                    res = []
                    break
                res.append(char)
        # if result is not empty add to valid cases
        if len(res) > 0:
            valid_cases.append(res)

    # find the max lenght of valid cases
    max_case = 0
    for i in valid_cases:
        max_case = max(max_case, len(i))

    # last condition to return 0 for invalid cases
    if len(valid_cases) == 0:
        return 0
    return max_case
