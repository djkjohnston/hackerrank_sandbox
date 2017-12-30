#angry-professor
#https://www.hackerrank.com/challenges/angry-professor/problem

#!/bin/python3

import sys

def angryProfessor(k, a):
    # Complete this function
    punctual = sum([student <= 0 for student in a])
        
    if punctual < k: #cancel class
        return "YES"
    else: #hold class
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
