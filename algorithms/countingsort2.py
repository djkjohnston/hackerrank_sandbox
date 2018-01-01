#countingsort2
#https://www.hackerrank.com/challenges/countingsort2/problem

#!/bin/python3

import sys

def countingSort(arr):
    # Complete this function
    sort_key = [0] * 100
    
    for i in arr:
        sort_key[i] += 1
    
    #print(sort_key)
    
    sorted_arr = []
    
    for i in range(100):
        for j in range(sort_key[i]):
            sorted_arr.append(i)
            
    return sorted_arr

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))


