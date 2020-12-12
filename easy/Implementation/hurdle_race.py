'''
    A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights,
    and the characters have a maximum height they can jump. There is a magic potion they can take that will
    increase their maximum jump height by 1 unit for each dose.
    How many doses of the potion must the character take to be able to jump all of the hurdles.
    If the character can already clear all of the hurdles, return 0.
'''

height = [1, 6, 3, 2, 5]

def hurdleRace(k, height):
    max_height = max(height)
    if k >= max_height:
        print(0)
    else:
        potion = max_height - k
        print(potion)

hurdleRace(4, height)