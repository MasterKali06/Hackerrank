'''
    Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers
    in S' is not evenly divisible by k.

    S: an array of integers
    k: an integer
'''



def nonDivisibleSubset(k, s):
    sums = []

    while len(s)>1:
        first = s[0]
        s.remove(first)
        for el in s:
            second = el + first
            sums.append(second)

    count = 0
    for i in sums:
        if i % k != 0:
            count +=1
    print(sums)
    print(count)



s = [1, 7, 2, 4]
t = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
x = [19, 10, 12, 10, 24, 25, 22]

#nonDivisibleSubset(3, s)
#nonDivisibleSubset(4, x)


# https://medium.com/@mrunankmistry52/non-divisible-subset-problem-comprehensive-explanation-c878a752f057
def nonDivisibleSubset1(k, s):
    # making a counter for ramainders of the array
    count = [0] * k

    for i in s:
        remainder = i % k
        count[remainder] += 1

    # case 1: we can take one number with the ramainder of zero
    ans = min(count[0], 1)

    # case 2: we can take one number of even numbers remainder
    if k % 2 == 0:  # even number
        ans += min(count[k//2], 1)

    # case 3: we check for the pairs and get the maximum number
    for i in range(1, k//2 + 1):
        if i != k - i:  # avoid over counting case 2
            ans += max(count[i], count[k - i])

    print(ans)

nonDivisibleSubset1(7, t)
