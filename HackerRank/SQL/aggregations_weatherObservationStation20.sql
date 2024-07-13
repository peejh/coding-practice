-- https://www.hackerrank.com/challenges/weather-observation-station-20
-- Difficulty: MEDIUM

-- Oracle
SELECT ROUND(MEDIAN(lat_n), 4)
  FROM station

-- MySQL solution 1
WITH
lats AS (
    SELECT ROW_NUMBER() OVER(ORDER BY lat_n) AS row_num, lat_n
    FROM STATION
)
SELECT
    CASE MOD(COUNT(*), 2)
    WHEN 1 THEN (
        SELECT ROUND(lat_n, 4)
          FROM lats
         WHERE row_num = (COUNT(*) + 1) / 2
    )
    WHEN 0 THEN (
        SELECT ROUND(AVG(lat_n), 4)
          FROM lats
         WHERE row_num IN (COUNT(*) / 2, (COUNT(*) + 2) / 2)
    )
    END
FROM lats

-- MySQL solution 2
WITH
lats AS (
    SELECT ROW_NUMBER() OVER(ORDER BY lat_n) AS row_num, lat_n, COUNT(*) OVER() AS tally
    FROM STATION
)
SELECT ROUND(AVG(lat_n), 4)
  FROM lats
 WHERE
  CASE MOD(tally, 2)
       WHEN 1
       THEN row_num = (tally + 1) / 2
       ELSE row_num IN (tally / 2, (tally + 2) / 2)
   END