#find-digits
#https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import sys

def findDigits(n):
    # Complete this function
    divisible_count = 0
    
    n_string = str(n)
    
    for digit in n_string:
        d = int(digit)
        
        if d == 0:
            continue
        elif d == 1:
            divisible_count += 1
        elif n % d == 0:
            divisible_count += 1
            
    return divisible_count
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
