-- https://www.hackerrank.com/challenges/sql-projects
-- Difficulty: MEDIUM

-- MS SQL Server
-- Difference between end_dates and row number gives the same
-- number for tasks that belong in the same project
WITH
orderedDates AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY end_date) rownum,
        start_date,
        end_date
    FROM projects
)
SELECT *
FROM (
    SELECT MIN(start_date) start_date, MAX(end_date) end_date
    FROM orderedDates
    GROUP BY DATEDIFF(dd, rownum, end_date) -- the key for grouping
) temp
ORDER BY DATEDIFF(dd, start_date, end_date), start_date