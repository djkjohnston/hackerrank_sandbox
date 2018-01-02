#append-and-delete
#https://www.hackerrank.com/challenges/append-and-delete/problem


#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    # Complete this function
    s_len = len(s)
    t_len = len(t)
    
    if s_len + t_len <= k:
        return "Yes"
    else:
        test_limit = min(s_len, t_len)

        root_match = 0

        for index in range(test_limit):
            if s[index] == t[index]:
                root_match += 1
            else:
                break

        letters_to_remove = s_len - root_match
        letters_to_add = t_len - root_match
        
        #print(root_match, letters_to_remove, letters_to_add)


        n_operations = letters_to_remove + letters_to_add

        if k < n_operations:
            return "No"
        elif k == n_operations:
            return "Yes"
        elif (k - n_operations) % 2 == 0:
            return "Yes"
        else:
            return "No"

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
