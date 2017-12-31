#strange-advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

import sys

def viralAdvertising(n):
    # Complete this function
    count = 0
    people = 5
    
    while n > 0:
        people = people // 2
        count += people 
        
        people *= 3
        n -= 1
    
    return count

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
