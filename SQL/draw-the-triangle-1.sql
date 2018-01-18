--https://www.hackerrank.com/challenges/draw-the-triangle-1/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
DECLARE @stars INT = 20
WHILE (@stars > 0) 
BEGIN
   PRINT REPLICATE('* ', @i) 
   SET @stars = @stars - 1
END