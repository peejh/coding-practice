-- https://www.hackerrank.com/challenges/weather-observation-station-15
-- Difficulty: EASY

-- Solution 1
SELECT ROUND(long_w, 4)
  FROM station
 WHERE lat_n = (
    SELECT MAX(lat_n) 
      FROM station
     WHERE lat_n < 137.2345
);

-- Solution 2
SELECT ROUND(long_w, 4)
  FROM station
 WHERE lat_n < 137.2345
 ORDER BY lat_n DESC
 LIMIT 1;