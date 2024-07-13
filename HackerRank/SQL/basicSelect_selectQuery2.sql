-- https://www.hackerrank.com/challenges/revising-the-select-query-2
-- Difficulty: EASY

SELECT name
  FROM city
 WHERE countrycode = 'USA'
   AND population > 120000