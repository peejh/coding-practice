-- https://www.hackerrank.com/challenges/weather-observation-station-4
-- Difficulty: EASY

SELECT COUNT(city) - COUNT(DISTINCT city)
  FROM station