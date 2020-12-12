'''
    https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=next-challenge&h_v=zen
'''

import string


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

def designerPdfViewer(h, word):
    alphabet = string.ascii_lowercase
    dic = {}
    for i in range(len(h)):
        dic[alphabet[i]] = h[i]

    words = []
    for i in range(len(word)):
        words.append(dic[word[i]])

    max_height = max(words)
    print(max_height * len(words))

word = "abc"
designerPdfViewer(h, word)