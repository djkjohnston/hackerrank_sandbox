# Bon Appétit
# https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    total = sum(ar)
    allergic = ar[k]
    
    correct = (total - allergic) / 2
    
    if correct == b:
        return "Bon Appetit"
    else:
        return int(b - correct)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
