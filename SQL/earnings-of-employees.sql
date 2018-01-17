--https://www.hackerrank.com/challenges/earnings-of-employees/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT
    months * salary,
    COUNT(*)
FROM
    employee
GROUP BY 
    months * salary
ORDER BY
    months * salary DESC
LIMIT
    1