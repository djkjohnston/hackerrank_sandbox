#Electronics Shop
#https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

import sys


def getMoneySpent(keyboards, drives, s):
    # Complete this function
    max_budget = 0
    
    for k in keyboards:
        for d in drives:
            cost = k+d
            
            if cost > max_budget and cost <= s:
                max_budget = k+d
    
    if max_budget == 0:
        return -1
    else:
        return max_budget

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
