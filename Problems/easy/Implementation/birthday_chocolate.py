

#i wrote this and didnt work properly for all tests
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        for x in range(1, m):
            if s[i] + s[x] == d:
                count += 1
            x += 1
        i += 1
    print(count)

birthday(chocolate, day, month)

#this one better :)
def birthday(s, d, m):
    result=0
    for i in range(len(s)):
        n=0
        count=0
        while(n<(m)):
            count+=s[i+n]
            n+=1
        if(count==d):
            result += 1
        if(i+n==len(s)):
            break
    return result