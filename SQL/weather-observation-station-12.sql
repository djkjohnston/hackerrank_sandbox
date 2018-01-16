--https://www.hackerrank.com/challenges/weather-observation-station-12/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT
    DISTINCT(city)
FROM
    station
WHERE
    lower(city) NOT LIKE '[aeiou]%' AND
    lower(city) NOT LIKE  '%[aeiou]'