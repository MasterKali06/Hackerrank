

ar = [10,20,20,10,10,30,50,10,20]
br = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

def sockMerchant(n, ar):
    d = {x:ar.count(x) for x in ar}
    D = []
    for i in d.values():
        D.append(i)

    count = 0
    for i in range(len(D)):
        x = int(D[i] / 2)
        count += x
        i+=1
    print(int(count))

sockMerchant(10,br)
sockMerchant(9,ar)
