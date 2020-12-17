'''
    https://www.hackerrank.com/challenges/taum-and-bday/problem

    int b: the number of black gifts
    int w: the number of white gifts
    int bc: the cost of a black gift
    int wc: the cost of a white gift
    int z: the cost to convert one color gift to the other color
'''

# easy peasy

def taumBday(b, w, bc, wc, z):

    total = []

    if bc + z < wc:
        whole = bc + z
        total.append((b * bc) + (w * whole))
    elif wc + z < bc:
        whole = wc + z
        total.append((b * whole) + (w * wc))
    else:
        total.append((b * bc) + (w * wc))

    return total