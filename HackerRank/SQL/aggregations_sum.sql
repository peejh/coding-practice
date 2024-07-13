-- https://www.hackerrank.com/challenges/revising-aggregations-sum
-- Difficulty: EASY

SELECT SUM(population)
  FROM city
 WHERE district = 'California'
 GROUP BY district