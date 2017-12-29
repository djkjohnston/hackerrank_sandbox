#designer-pdf-viewer
#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#!/bin/python3

import sys

def designerPdfViewer(h, word):
    # Complete this function
    letters = [ord(letter)-97 for letter in word]
    heights = [h[letter] for letter in letters]

    max_height = max(heights)
    area = max_height * len(word)
    
    return area
    

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
