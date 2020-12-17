'''
    https://www.hackerrank.com/challenges/counting-valleys/problem
'''

exam1 = ['U','D','D','D','U','U','U','D','D','U']
def countingValley(steps,path):
    sealevel = 0
    vallycount = 0
    d = {'U':1 , 'D':-1}
    for step in path:
        sealevel += d[step]
        if sealevel == 0 and step == 'U':
            vallycount += 1
    print(vallycount)

countingValley('9',exam1)