'''
    You are in charge of the cake for a child's birthday.
    You have decided the cake will have one candle for each year of their total age.
    They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
'''


ar = [3 , 3, 2, 3]

def birthdayCakeCandles(ar):
    length = len(ar)
    big = max(ar)
    max_i = 0
    for i in range(length):
        if ar[i] == big:
            max_i += 1

    print(max_i)


birthdayCakeCandles(ar)