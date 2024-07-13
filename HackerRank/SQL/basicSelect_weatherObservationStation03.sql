-- https://www.hackerrank.com/challenges/weather-observation-station-3
-- Difficulty: EASY

SELECT DISTINCT city
  FROM station
 WHERE MOD(id, 2) = 0