'''
    https://www.hackerrank.com/challenges/library-fine/problem
'''

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1==y2 and m1==m2 and d1>d2:
        fine = (d2 - d1) * 15
    elif y1==y2 and m1>m2:
        fine = m1 * 500
    elif y1>y2:
        fine = 10000
    else:
        fine = 0

    return fine