-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function
-- Difficulty: EASY

SELECT AVG(population)
  FROM city
 WHERE district = 'California'
 GROUP BY district