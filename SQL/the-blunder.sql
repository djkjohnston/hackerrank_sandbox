--https://www.hackerrank.com/challenges/the-blunder/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT
    CEILING(
        AVG(salary - CAST(REPLACE(CAST(salary AS CHAR), '0', '') AS numeric))
    )
FROM
    employees