-- https://www.hackerrank.com/challenges/japan-population
-- Difficulty: EASY

SELECT SUM(population)
  FROM city
 WHERE countrycode = 'JPN'