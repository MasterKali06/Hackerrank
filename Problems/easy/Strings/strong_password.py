"""
    https://www.hackerrank.com/challenges/strong-password/problem

    int n: the length of the password
    string password: the password to test
"""


def minimumNumber(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # make a list of zeroes and for each condition passed make 0 --> 1
    # we can use islower(), isdigit(), isupper() for the conditions too
    count = 0
    res = [0, 0, 0, 0]
    for char in password:
        if char in numbers:
            res[0] = 1
        elif char in lower_case:
            res[1] = 1
        if char in upper_case:
            res[2] = 1
        if char in special_characters:
            res[3] = 1

    # count the zeroes to know how many conditions we need to add to password
    count += res.count(0)
    # last condition --> ( at last we see if its less than n or not )
    if n < 6:
        if count < (6 - n):
            count = 6 - n
    return count

