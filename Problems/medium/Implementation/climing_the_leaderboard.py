'''
    An arcade game player wants to climb to the top of the leaderboard and track their ranking.
    The game uses Dense Ranking, so its leaderboard works like this:
    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
'''

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]


def climbingLeaderboard(ranked, player):

    result = []
    dic = {}
    uniq_ranked = []

    # making a list of uniq scores
    for uniq in ranked:
        if uniq not in uniq_ranked:
            uniq_ranked.append(uniq)
    print(uniq_ranked)

    # making a dictionary
    i = 1
    for x in uniq_ranked:
        dic[x] = i
        i += 1
    print(dic)

    for i in player:
        for j in uniq_ranked:
            if i < min(uniq_ranked):
                result.append(len(uniq_ranked)+ 1)
                break
            if i >= j:
                result.append(dic[j])
                break
    print(result)

#climbingLeaderboard(ranked, player)

# more speedy .. cheated this one
def climbingLeaderboard1(ranked, player):

    uniq_ranked = sorted(list(set(ranked)), reverse=True)
    player.sort(reverse = True)

    result = []
    l = len(uniq_ranked)
    j = 0

    for i in range(len(player)):
        while j<l and player[i]<uniq_ranked[j]:
            j += 1
        result.append(j + 1)

    print(result[::-1])


climbingLeaderboard1(ranked, player)