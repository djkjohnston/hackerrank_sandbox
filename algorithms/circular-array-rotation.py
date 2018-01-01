# circular-array-rotation
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

#!/bin/python3

import sys

def circularArrayRotation(a, k, m):
    # Complete this function
    # a = array to rotate
    # k = number of rotations
    # m = index
    
    remainder = k % len(a)
    
    rotated_list = a[-remainder:]
    rotated_list.extend(a[0:-remainder])
    
    #print(remainder, rotated_list)
    
    queries = []
    
    for i in m:
        queries.append(rotated_list[i])
    
    return queries

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, k, m)
    print ("\n".join(map(str, result)))


