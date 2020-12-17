"""
    https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""
import string


# it was a good try .. but in some cases it didnt work because i dont get the question
# according to this code abdc --> adbc but the right answer is acbd ..
# i dont know how c goes 2 points back and this is the minimum move :)
def biggerIsGreater(w):
    dic = {}
    alph = string.ascii_lowercase
    j = 0
    while j < len(alph):
        for i in alph:
            dic[i] = j
            j += 1

    w = list(w)
    w = w[::-1]
    greater_index = 0
    index = 1

    for char in w:
        while index < len(w):
            if dic.get(char) > dic.get(w[index]):
                greater_index = index
                break
            index += 1
        if greater_index != 0:
            break

    if greater_index == 0:
        print("no answer")
    else:
        w[greater_index - 1], w[greater_index] = w[greater_index], w[greater_index - 1]

        print("".join(w[::-1]))


# this will work but i didnt have the time to understand the problem logic
def i_didnt_understand_this_prob(arr):
    arr = list(arr)
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    print(i)
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    print(j)

    arr[i:] = arr[len(arr) - 1:i - 1: -1]
    return "".join(arr)
