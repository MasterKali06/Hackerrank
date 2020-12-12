'''
    https://www.hackerrank.com/challenges/encryption/problem
'''
from collections import defaultdict
import math
s = "if man was meant to stay on the ground god would have given us roots"

def encryption(s):
    s = s.replace(" ", "")
    l = math.sqrt(len(s))
    r = math.floor(l)
    c = math.ceil(l)

    dic = defaultdict(str)
    for i in range(0, len(s), c):
        sub = s[i:i+c]
        # adding sub to dictionary
        for j in range(len(sub)):
            dic[j] += sub[j]

    d = list(dic.values())
    print(" ".join(d))


#encryption(s)

# :)))))))))))
def enc_cool(s):
    sm = s.replace(" ", "")
    r = math.floor(math.sqrt(len(sm)))
    c = math.ceil(math.sqrt(len(sm)))
    for i in range(c):
        print(sm[i::c], end=" ")

enc_cool(s)