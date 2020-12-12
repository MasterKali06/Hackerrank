'''
    https://www.hackerrank.com/challenges/magic-square-forming/problem
'''


import sys

s = [[2,9,8], [4,2,7], [5,6,7]]

# failed attemp i didnt consider the smaller picks that fit the answer
def formingMagicSquare(s):
    magic_num = []
    for i in s:
        magic_num.append(sum(i))
    magic = max(magic_num)

    result = (magic * 3) - sum(magic_num)
    print(magic_num)

#formingMagicSquare(s)

# failed attemp number 2 :)
def formingMagicSquare1(s):
    magic_num = []
    for i in s:
        magic_num.append(sum(i))

    x = (int(sum(magic_num) / 3))
    sum_sum = abs(magic_num[0] - x) + abs(magic_num[1] - x) + abs(magic_num[2] - x)
    final = sum_sum + (sum(magic_num) % 3)
    print(final)

#formingMagicSquare1(s)

# some videos suggest to download all the square matrixes in a 3*3 matrixes and compare ours with them
# and then find the minimum cost to change our matrix to a magic square one

# last chance  { failed: better but we will encounter the same numbers in matrix that will ruin the answer in some cases }
def formingMagicSquare3(s):
    sum_list = []
    for i in s:
        sum_list.append(sum(i))

    magic_nums = []
    x = 15
    for i in sum_list:
        res = abs(x - i)
        magic_nums.append(res)
    print(sum(magic_nums))



# at last i cheated :)
def formingMagicSquare2(s):
    magic_square = [[8,1,6,3,5,7,4,9,2], [4,3,8,9,5,1,2,7,6],
                    [2,9,4,7,5,3,6,1,8], [6,7,2,1,5,9,8,3,4],
                    [6,1,8,7,5,3,2,9,4], [8,3,4,1,5,9,6,7,2],
                    [4,9,2,3,5,7,8,1,6], [2,7,6,9,5,1,4,3,8]]
    s = sum(s, [])  # this will change 2d matrix to 1d
    minimumcost = sys.maxsize

    for mag in magic_square:
        diff = 0
        for i,j in zip(s,mag):
            diff += abs(i - j)

        minimumcost = min(minimumcost, diff)

    print(minimumcost)

formingMagicSquare3(s)
