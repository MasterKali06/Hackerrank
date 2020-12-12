'''
    Given a chocolate bar, two children, Lily and Ron, are determining how to share it.
    Each of the squares has an integer on it.
    Lily decides to share a contiguous segment of the bar selected such that:
    The length of the segment matches Ron's birth month, and,The sum of the integers on the squares is equal to his birth day.
    You must determine how many ways she can divide the chocolate.
'''

example = [1, 2, 1, 3, 2]

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:m]) == d:
            count += 1
        i += 1
        m += 1
    print(count)

birthday(example, 3, 2)