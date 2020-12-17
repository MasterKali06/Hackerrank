'''
    There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
    1- The elements of the first array are all factors of the integer being considered
    2 -The integer being considered is a factor of all elements of the second array
    These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
'''



a = [2,4]
b = [16,32,96]
'''
factors = []
c = []
for i in range(a[-1],b[0]):
    c.append(i)

for i in range(len(b)):
    for x in range(len(c)):

        if b[i] % c[x] == 0:
            factors.append(c[x])
            x += 1
    i+=1
factors = list(set(factors))
print(factors)
z = []
count = 0
for i in range(len(factors)):
    for x in range(len(a)):
        if factors[i] % a[x] == 0:
            z.append(factors[i])
            print(z)
            count += 1
            x += 1
    i+=1

print(count)
'''
#this was my try that comes to no end lol!!!

'''
ct = 0
c = []
for i in range(a[-1],b[1]):
    for j in a:
        if i%j !=0:
            break
        else:
            for k in b:
                if k%i != 0:
                    break
            else:
                c.append(i)
print(len(set(c)))
'''
#second try no luck

#copied this from google and it worked :((
from functools import reduce

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm, min_gcd + 1, max_lcm) if min_gcd % x == 0])

    return count

#print(getTotalX(a,b))