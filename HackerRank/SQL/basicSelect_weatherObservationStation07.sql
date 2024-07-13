-- https://www.hackerrank.com/challenges/weather-observation-station-7
-- Difficulty: EASY

-- Solution 1
SELECT DISTINCT city
  FROM station
 WHERE RIGHT(city, 1) IN ('a', 'e', 'i', 'o', 'u');

-- Solution 2
SELECT DISTINCT city
  FROM station
 WHERE city REGEXP '[aeiou]$';