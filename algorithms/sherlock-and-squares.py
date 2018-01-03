#sherlock-and-squares
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
#!/bin/python3

import sys
import math

def squares(a, b):
    # Complete this function
    
    a_ceil = math.ceil(a ** 0.5)
    b_floor = math.floor(b ** 0.5)
            
    return b_floor - a_ceil + 1

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
