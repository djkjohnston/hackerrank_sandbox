#save-the-prisoner
#https://www.hackerrank.com/challenges/save-the-prisoner/problem

#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    # n = number of prisoners
    # m = number of sweets
    # s = starting id
    
    sweets_remaining = m % n
    
    prisoner = (s - 1 + sweets_remaining - 1) % n
    
    return prisoner +1

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

