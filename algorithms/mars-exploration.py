# mars-exploration
#https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import sys

def marsExploration(s):
    # Complete this function
    changed_letters = 0
    
    #print(s[0::3])
    #print(s[1::3])
    #print(s[2::3])
    
    # S
    for letter in s[0::3]: # every third letter starting with the first letter (0th index)
        if letter != "S":
            changed_letters += 1
    
    # O
    for letter in s[1::3]: # every third letter starting with the second letter (first index)
        if letter != "O":
            changed_letters += 1
    
    # S
    for letter in s[2::3]: # every third letter starting with the third letter (second index)
        if letter != "S":
            changed_letters += 1
            
    return changed_letters

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
