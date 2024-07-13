-- https://www.hackerrank.com/challenges/revising-the-select-query
-- Difficulty: EASY

SELECT *
  FROM city
 WHERE countrycode = 'USA'
   AND population > 100000