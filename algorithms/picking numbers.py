#picking numbers
#https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a_set = set(a)

diff_count = []

for testing_val in a_set:
    tmp = sum([i in (testing_val, testing_val+1) for i in a])
    diff_count.append(tmp)
    
print(max(diff_count))