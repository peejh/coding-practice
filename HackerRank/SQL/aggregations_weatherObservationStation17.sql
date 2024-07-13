-- https://www.hackerrank.com/challenges/weather-observation-station-17
-- Difficulty: EASY

SELECT ROUND(long_w, 4)
  FROM station
 WHERE lat_n > 38.7780
 ORDER BY lat_N
 LIMIT 1