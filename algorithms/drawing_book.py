# Drawing Book
# https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    from_start = p // 2
    if n % 2 == 0:
        from_end = (n - p + 1) // 2
    else:
        from_end = (n - p) // 2
    
    return min(from_start, from_end)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
