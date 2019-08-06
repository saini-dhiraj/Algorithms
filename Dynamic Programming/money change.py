# python3

import math
money = int(input())


def moneydp(money, coins):
    ptive=math.inf
    min_num_change=[0]
    for m in range(1, money+1):
        min_num_change.append(ptive)
        for i in range(0,len(coins)):
            if m >= coins[i]:
                num_coins= min_num_change[m-coins[i]]+1
                if num_coins<min_num_change[m]:
                    min_num_change[m]=num_coins

    return min_num_change[money]


coins = [1,3,4]


print(moneydp(money,coins))
