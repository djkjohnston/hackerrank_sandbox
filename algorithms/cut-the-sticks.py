#cut-the-sticks
#https://www.hackerrank.com/challenges/cut-the-sticks/problem


#!/bin/python3

import sys

def cutTheSticks(arr):
    # Complete this function
    n = len(arr)
    
    stick_count = []
    
    while n > 0:
        stick_count.append(n)
        
        cut = min(arr)
        arr = [i - cut for i in arr]
        arr = [i for i in arr if i > 0]
        
        n = len(arr)
    
    return stick_count

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr)
    print ("\n".join(map(str, result)))


