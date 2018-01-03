#library-fine
#https://www.hackerrank.com/challenges/library-fine/problem

#!/bin/python3

import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Complete this function
    y_late = y1 - y2
    m_late = m1 - m2
    d_late = d1 - d2
    
    if y_late > 0: # year late
        return 10000
    elif y_late == 0 and m_late > 0:
        return 500 * m_late
    elif y_late == 0 and m_late == 0 and d_late > 0:
        return 15 * d_late
    else:
        return 0

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
