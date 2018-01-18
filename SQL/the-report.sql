--https://www.hackerrank.com/challenges/the-report/problem

/*
Enter your query here.
*/

SELECT
    CASE WHEN (grade < 8) THEN NULL ELSE name END,
    grade,
    marks
FROM
    students
JOIN
    grades
ON
    marks BETWEEN min_mark and max_mark
ORDER BY
    grade DESC, name ASC