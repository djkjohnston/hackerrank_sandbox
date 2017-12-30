#beautiful-days-at-the-movies
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

import sys

def beautifulDays(i, j, k):
    # Complete this function
    
    def reverse(d):
        d = str(d)
        d = d[::-1]
        d = int(d)
        return d
    
    diff = j - i
    
    count = 0
    
    for n in range(diff + 1):
        day = n + i
        rev = reverse(day)
        
        beautiful = abs(day - rev) % k == 0
        
        if beautiful:
            count += 1
    
    return count
        
        

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
