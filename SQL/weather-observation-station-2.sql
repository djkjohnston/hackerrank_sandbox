--https://www.hackerrank.com/challenges/weather-observation-station-2/problem

/*
Enter your query here.
*/
SELECT
    ROUND(SUM(lat_n),2) AS lat,
    ROUND(SUM(long_w),2) AS lon
FROM
    station 	