"""
    https://www.hackerrank.com/challenges/camelcase/problem

    string s: the string to analyze
"""
import string


def camelcase(s):
    count = 1
    upper = string.ascii_uppercase
    for i in s:
        if i in upper:
            count += 1

    return count
