-- https://www.hackerrank.com/challenges/weather-observation-station-14
-- Difficulty: EASY

SELECT TRUNCATE(MAX(lat_n), 4)
  FROM station
 WHERE lat_n < 137.2345