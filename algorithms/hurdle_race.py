# the hurdle race
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

#!/bin/python3

import sys

def hurdleRace(k, height):
    # Complete this function
    max_height = max(height)
    
    diff = max_height - k
    
    if diff > 0:
        return diff
    else:
        return 0

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
