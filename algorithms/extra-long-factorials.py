#extra-long-factorials
#https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import sys
import math

def extraLongFactorials(n):
    # Complete this function
    x = math.factorial(n)
    print(x)
    
if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
