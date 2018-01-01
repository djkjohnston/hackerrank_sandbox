#camelcase
#https://www.hackerrank.com/challenges/camelcase/problem

#!/bin/python3

import sys

def camelcase(s):
    # Complete this function
    
    cap_count = 1
    
    for letter in s:
        if letter.isupper():
            cap_count += 1
            
    return cap_count

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
