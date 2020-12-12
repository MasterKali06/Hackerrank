'''
    An integer d is a divisor of an integer n if the remainder of n % d = 0.
    Given an integer, for each digit that makes up the integer determine whether it is a divisor.
    Count the number of divisors occurring within the integer.
'''



def findDigits(n):

    count = 0
    n = str(n)

    for i in range(len(n)):
        if int(n[i]) != 0 and int(n) % int(n[i]) == 0:
            count += 1
        i += 1

    print(count)

findDigits(1012)