--https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

/*
id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

*/
WITH wand_comp AS (
    SELECT
        id,
        age,
        coins_needed,
        power,
        RANK() OVER(PARTITION BY age, power ORDER BY coins_needed ASC) as rank
    FROM
        wands
    JOIN wands_property ON wands.code = wands_property.code
    WHERE
        is_evil = 0
    )


SELECT
    id,
    age,
    coins_needed,
    power
FROM
    wand_comp
WHERE
    rank =1
ORDER BY
    power DESC, age DESC
