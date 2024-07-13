-- https://www.hackerrank.com/challenges/draw-the-triangle-1
-- Difficulty: EASY

-- MySQL
DECLARE i INT DEFAULT 20;
WHILE i > 0
DO
    SELECT REPEAT('* ', i)
    SET i = i - 1;
END WHILE

-- MS SQL Server
DECLARE @i INT = 20;
WHILE @i > 0
BEGIN
    PRINT REPLICATE('* ', @i)
    SET @i = @i - 1;
END