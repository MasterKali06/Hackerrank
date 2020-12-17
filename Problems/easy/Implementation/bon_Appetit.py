

def bonAppetit(bill, k, b):
    sara_share = (sum(bill) - bill[k]) / 2
    if sara_share == b:
        print("Bon Appetit")
    else:
        x = b - sara_share
        print(int(x))

bonAppetit(bill,k,b)