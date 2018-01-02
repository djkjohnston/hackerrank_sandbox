#permutation-equation
#https://www.hackerrank.com/challenges/permutation-equation/problem

#!/bin/python3

import sys

def permutationEquation(p):
    # Complete this function
    
    ys = []
    
    for i in range(1, len(p)+1):
        index_0 = p.index(i)
        index_1 = p.index(index_0 + 1)
        
        ys.append(index_1 + 1)
        
    return ys

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))


