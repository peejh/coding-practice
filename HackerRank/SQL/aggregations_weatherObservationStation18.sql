-- https://www.hackerrank.com/challenges/weather-observation-station-18
-- Difficulty: MEDIUM

SELECT ROUND((p.c - p.a) + (p.d - p.b), 4)
FROM (
    SELECT MIN(lat_n) AS a, MIN(long_w) AS b, MAX(lat_n) AS c, MAX(long_w) AS d
    FROM station
) p;

-- More succinct
SELECT ROUND((MAX(lat_n) - MIN(lat_n)) + (MAX(long_w) - MIN(long_w)), 4)
FROM station;