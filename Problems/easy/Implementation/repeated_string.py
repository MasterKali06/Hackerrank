'''
    There is a string, s, of lowercase English letters that is repeated infinitely many times.
    Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
'''

def repeatedString(s, n):
    count = 0

    for i in range(len(s)):
        if s[i] == "a":
         count += 1

    round_res = count * (n // len(s))
    new_count = 0

    if n % len(s) == 0:
        res = round_res
    else:
        for i in range(0, (n % len(s))):
            if s[i] == "a":
                new_count += 1
        res = round_res + new_count
    print(res)


test_cast = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
n = 549382313570
test = n % len(test_cast)

count = 0
for i in range(0, 100):
    if test_cast[i] == "a":
        count += 1
res = 3 * (n // len(test_cast))
print(res)

s = "aaa"
repeatedString(test_cast, n)