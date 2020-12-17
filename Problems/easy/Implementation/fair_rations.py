"""
    https://www.hackerrank.com/challenges/fair-rations/problem
"""


# worst of the problems i think
# if the sum of people is even its possible and if the sum is odd its impossible and the asnwer is NO
def fairRations(B):
    count = 0

    if sum(B) % 2 != 0:
        return "NO"

    else:
        # the logic is u add to odd numbers and the number after them in a loop ( next number become odd )
        for i in range(len(B)):
            if B[i] % 2 != 0:
                B[i] += 1
                B[i + 1] += 1
                count += 2
        return count
