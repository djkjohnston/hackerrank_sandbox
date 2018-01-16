--https://www.hackerrank.com/challenges/weather-observation-station-5/problem

/*
Enter your query here.
*/

SELECT
    city,
    LENGTH(city)
FROM
    station
ORDER BY
    LENGTH(city) ASC, city ASC
LIMIT 1;

SELECT
    city,
    LENGTH(city)
FROM
    station
ORDER BY
    LENGTH(city) DESC, city ASC
LIMIT 1;