"""
    https://www.hackerrank.com/challenges/the-time-in-words/problem

    int h: the hour of the day
    int m: the minutes after the hour
"""


# didnt think much on this, i think there are better ways to do this
def timeInWords(h, m):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen",
             "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three",
             "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight",
             "twenty nine", "half"]

    dic = {}
    for i in range(1,31):
        dic[i] = words[i - 1]

    j = 0
    dic2 = {}
    for i in reversed(range(31, 60)):
        dic2[i] = words[j]
        j += 1

    if m == 0:
        return dic[h] + " o' clock"
    elif m == 1:
        return dic[m] + " minute past " + dic[h]
    elif m == 30:
        return dic[30] + " past " + dic[h]
    elif m == 15:
        return dic[15] + " past " + dic[h]
    elif m == 45:
        return dic2[45] + " to " + dic[h+1]
    elif m == 59:
        return dic2[m] + " minute to " + dic[h+1]
    elif 1 < m < 30:
        return dic[m] + " minutes past " + dic[h]
    elif 30 < m < 60:
        return dic2[m] + " minutes to " + dic[h+1]
