#Sock Merchant
#https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    sock_set = set(ar)
    
    pairs = 0
    
    for color in sock_set:
        color_count = sum([sock == color for sock in ar])
        pairs += color_count // 2
        
    return pairs

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
