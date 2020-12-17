'''
    Given the scores for a season, find and print the number of times Maria breaks her records for most
    and least points scored during the season.
'''


test = [10 , 6, 21, 36, 10, 28, 35, 5 ,24, 42]

def breakingRecords(scores):
    first = [scores[0]]
    max_i = 0
    min_i = 0
    for i in range(len(scores)):
        if scores[i] > max(first):
            max_i += 1
        if scores[i] < min(first):
            min_i += 1

        first.append(scores[i])
        i += 1

    print(str(max_i) + ' ' + str(min_i))

breakingRecords(test)
