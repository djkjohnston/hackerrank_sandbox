# cat and mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3

import sys

def mouse_chase(x, y, z):
    dist_a = abs(z-x)
    dist_b = abs(z-y)
    
    if dist_a < dist_b:
        return("Cat A")
    elif dist_b < dist_a:
        return("Cat B")
    else:
        return("Mouse C")

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    result = mouse_chase(x, y, z)
    
    print(result)
