-- https://www.hackerrank.com/challenges/draw-the-triangle-2
-- Difficulty: EASY

-- MS SQL Server
DECLARE @i INT = 1;
WHILE @i < 21
BEGIN
    PRINT REPLICATE('* ', @i)
    SET @i = @i + 1;
END