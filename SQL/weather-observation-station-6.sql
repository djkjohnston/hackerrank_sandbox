--https://www.hackerrank.com/challenges/weather-observation-station-6/problem

/*
Enter your query here.
*/

SELECT
    city
FROM
    station
WHERE
    lower(city) LIKE 'a%' OR
    lower(city) LIKE 'e%' OR
    lower(city) LIKE 'i%' OR
    lower(city) LIKE 'o%' OR
    lower(city) LIKE 'u%'