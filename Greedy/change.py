# python3

money  = int(input())


def GreedyChange(money):
    change = 0
    while money>0:

        if money>=10:
            coin = 10
        elif money>=5:
            coin = 5
        else:
            coin = 1
        change = change+1
        money = money-coin
    print(change)

GreedyChange(money)