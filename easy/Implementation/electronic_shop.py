'''
    A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
    Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
    If it is not possible to buy both items, return -1 .
'''


keboards = [1, 5]
drives = [3, 7]

def getMoneySpent(keyboards, drives, b):

    element = []
    for keyboard in keyboards:
        for drive in drives:
            element.append(drive + keyboard)

    purchase = []
    for el in element:
        if el <= b:
            purchase.append(el)


    if len(purchase) == 0:
        print("-1")
    else:
        print(max(purchase))

getMoneySpent(keboards, drives, 5)