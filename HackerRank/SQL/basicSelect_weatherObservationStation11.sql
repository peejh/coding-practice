-- https://www.hackerrank.com/challenges/weather-observation-station-11
-- Difficulty: EASY

SELECT DISTINCT city
  FROM station
 WHERE city REGEXP '^[^aeiou]'
    OR city REGEXP '[^aeiou]$'