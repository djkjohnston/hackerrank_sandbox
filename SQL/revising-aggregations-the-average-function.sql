--https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT
    AVG(population)
FROM
    city
WHERE
    lower(district) = 'california'