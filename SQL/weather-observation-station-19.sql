--https://www.hackerrank.com/challenges/weather-observation-station-19/problem

/*
Enter your query here.
*/

SELECT
    ROUND(
        SQRT(
            POWER(MAX(lat_n) - MIN(lat_n),2) + 
            POWER(MAX(long_w) - MIN(long_w),2)
            )
        ,4)
FROM
    station;