"""
    https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""


def kaprekarNumbers(p, q):
    check_list = []

    # defining a check function
    def check(number):
        sqr = str(number**2)
        d = len(sqr) // 2

        # handing the cases < 9 ( just 1 is kaprekar before 9)
        if len(sqr) == 1 and len(sqr) < 9:
            if "1" in sqr:
                check_list.append("1")
        elif int(sqr[:d]) + int(sqr[d:]) == number:
            check_list.append(str(number))

    for num in range(p, q+1):
        check(num)

    if len(check_list) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(check_list))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)