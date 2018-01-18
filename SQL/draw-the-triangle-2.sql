--https://www.hackerrank.com/challenges/draw-the-triangle-2/problem


DECLARE @stars INT = 1
WHILE (@stars < 21) 
BEGIN
   PRINT REPLICATE('* ', @stars) 
   SET @stars = @stars + 1
END