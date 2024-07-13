-- https://www.hackerrank.com/challenges/weather-observation-station-9
-- Difficulty: EASY

-- Solution 1
SELECT DISTINCT city
  FROM station
 WHERE city REGEXP '^[^aeiou]';

-- Solution 2
SELECT DISTINCT city
  FROM station
 WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');