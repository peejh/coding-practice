-- https://www.hackerrank.com/challenges/weather-observation-station-19
-- Difficulty: MEDIUM

SELECT ROUND(SQRT(POWER(p.b - p.a, 2) + POWER(p.d - p.c, 2)), 4)
FROM (
    SELECT MIN(lat_n) AS a, MAX(lat_n) AS b, MIN(long_w) AS c,  MAX(long_w) AS d
    FROM station
) p