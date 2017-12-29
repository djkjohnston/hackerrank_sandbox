#utopian-tree
#https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

import sys

def utopianTree(n):
    # Complete this function
    height = 1
    
    while True:
        if n == 0:
            return height
        
        # double cycle
        height *= 2
        n -= 1
        
        if n == 0:
            return height
        height +=1
        n -= 1
        
        
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
