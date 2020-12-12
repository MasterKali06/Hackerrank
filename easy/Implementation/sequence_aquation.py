'''
    https://www.hackerrank.com/challenges/permutation-equation/problem
'''

p = [4, 3, 5, 1, 2]
n = 5

def permutationEquation(p, n):
    dic = {}
    count = 1
    for i in p:
        dic[i] = count
        count += 1
    print(dic)

    for x in range(1, n+1):
        first_val = dic[x]
        result = dic[first_val]
        x += 1
        print(result)


permutationEquation(p, n)