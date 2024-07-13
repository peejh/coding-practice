-- https://www.hackerrank.com/challenges/weather-observation-station-5
-- Difficulty: EASY

SELECT city, LENGTH(city) AS name_length
  FROM station
 ORDER BY name_length ASC, city ASC
 LIMIT 1;

SELECT city, LENGTH(city) AS name_length
  FROM station
 ORDER BY name_length DESC, city ASC
 LIMIT 1;