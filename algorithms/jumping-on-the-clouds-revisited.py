#jumping-on-the-clouds-revisited
#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

#!/bin/python3

import sys

def jumpingOnClouds(c, k):
    # Complete this function
    n = len(c)
    e = 100
    current_cloud = 0
    
    while e >= 0:
        #print(current_cloud, e)
        
        #jump!
        current_cloud = (current_cloud + k) % n
        e -= 1
        
        #thunder cloud
        if c[current_cloud] == 1:
            e -= 2    
            
        # land on cloud 0
        if current_cloud == 0:
            break
   
    return e

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
