'''
    https://www.hackerrank.com/challenges/acm-icpc-team/problem
    n : the number of attendees
    m : the number of topics
    topics : array of bit strings contain 1 and 0s for known and unknown topic for attendee
'''

from itertools import combinations

def acmTeam(topic):

    result = []
    dic = {}
    for i in range(n):
        dic[i] = topic[i]

    teams = []
    count_list = []
    for i in range(n):
        teams.append(i)

    # combination give a list of tuples with non-repeated combinations
    for j in combinations(teams, 2):
        count = 0
        sums = int(dic[j[0]]) + int(dic[j[1]])
        for i in str(sums):
            if i == "1" or i == "2":
                count += 1
        count_list.append(count)


    result.append(max(count_list))
    result.append(count_list.count(max(count_list)))
    print(result)


if __name__ == "__main__":
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)