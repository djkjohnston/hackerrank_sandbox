--https://www.hackerrank.com/challenges/binary-search-tree-1/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

WITH nodes as (
    SELECT n AS node FROM bst WHERE n IS NOT NULL
    UNION
    SELECT p AS node FROM bst WHERE p IS NOT NULL)

SELECT
    node,
    CASE
        WHEN ((SELECT COUNT(p) FROM bst WHERE p=node)=0) THEN 'Leaf'
        WHEN ((SELECT p FROM bst WHERE n=node) IS NULL) THEN 'Root'
        ELSE 'Inner'
        END
FROM
    nodes
ORDER BY
    node