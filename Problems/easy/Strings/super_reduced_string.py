"""
    https://www.hackerrank.com/challenges/reduced-string/problem

    string s: a string to reduce
"""


def superReducedString(s):
    s = list(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            del s[i]
            del s[i]
            i = 0
            if len(s) == 0:
                return "Empty String"
        else:
            i += 1
    return "".join(s)
