'''
    https://www.hackerrank.com/challenges/save-the-prisoner/problem
    n : the number of prisoners
    m : the number of sweets
    s : the chair number to start passing out treats at
'''
# first try failed .. then i changed it a bit after cheating and it worked

def saveThePrisoner(n, m, s):
    default_loop = (s+m-1) % n
    if default_loop == 0:
        default_loop = n

    print(default_loop)

#saveThePrisoner(999999999   , 999999999   , 1)

# second try
def saveThePrisoner1(n, m, s):
    default_loop = m % n
    if n + s < n:
        sweet_chair = s + m -1
    if default_loop == 0:
        sweet_chair = s - 1
    if default_loop > 0:
        sweet_chair = s + default_loop - 1

    print(sweet_chair)

saveThePrisoner(5, 2, 2)