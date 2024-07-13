-- https://www.hackerrank.com/challenges/weather-observation-station-6
-- Difficulty: EASY

-- Solution 1
SELECT DISTINCT city
  FROM station
 WHERE SUBSTR(city, 1, 1) IN ('a', 'e', 'i', 'o', 'u');

-- Solution 2
SELECT DISTINCT city
  FROM station
 WHERE city REGEXP '^[aeiou]';