# counting valleys
# https://www.hackerrank.com/challenges/counting-valleys/problem

import sys

n = int(input().strip())
ar = list(str(input().strip()))

level = 0
valley_count = 0

for move in ar:
    if move == "U":
        level += 1
        
        if level == 0:
            valley_count += 1
    else:
        level -= 1
        
print(valley_count)
            