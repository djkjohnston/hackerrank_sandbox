--https://www.hackerrank.com/challenges/full-score/problem

/*
Enter your query here.
*/

SELECT
    distinct(submissions.hacker_id),
    hackers.name
FROM
    submissions
JOIN hackers ON hackers.hacker_id = submissions.hacker_id
JOIN challenges ON submissions.challenge_id = challenges.challenge_id
JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
WHERE
    submissions.score = difficulty.score
GROUP BY
    submissions.hacker_id, hackers.name
HAVING
    count(submissions.score) > 1
ORDER BY
    count(submissions.score) DESC, hackers.hacker_id ASC
