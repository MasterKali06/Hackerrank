'''
    The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
    Each summer, its height increases by 1 meter.
'''


def utopianTree(n):
    height = 1
    for i in range(0,n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
        i += 1
    print(height)

utopianTree(4)