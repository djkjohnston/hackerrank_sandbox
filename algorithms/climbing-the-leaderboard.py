#climbing-the-leaderboard
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    # Write Your Code Here
    rank_scores = list(set(scores))
    rank_scores.sort()
    
    #print(rank_scores)
    #print(alice)
    
    rank_len = len(rank_scores)
    rank_i = 0 

    for a in alice:
        while (rank_i < rank_len) and (a >= rank_scores[rank_i]):
            rank_i += 1
        current_rank = rank_len - rank_i + 1
        print(current_rank)
        