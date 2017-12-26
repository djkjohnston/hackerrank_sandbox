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
    
    for a_score in alice:
        tmp_rank = sum([scoreboard > a_score for scoreboard in rank_scores]) + 1
        print(tmp_rank)
