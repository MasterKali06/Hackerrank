'''
 do to the long discription see the link bellow
 https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''


def dayOfProgrammer(year):
    year = int(year)
    if (year) % 4 == 0:
        print("12.09." + str(year))
    else:
        print("13.09." + str(year))

year = 1980
dayOfProgrammer(year)

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year