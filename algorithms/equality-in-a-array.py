#equality-in-a-array
#https://www.hackerrank.com/challenges/equality-in-a-array/problem

#!/bin/python3

import sys

def equalizeArray(arr):
    # Complete this function
    value_counts = [arr.count(x) for x in set(arr)]
    
    #print(value_counts)
    
    return sum(value_counts) - max(value_counts)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
