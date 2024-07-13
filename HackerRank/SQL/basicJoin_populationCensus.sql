-- https://www.hackerrank.com/challenges/asian-population
-- Difficulty: EASY

SELECT SUM(ci.population)
  FROM city ci
 INNER JOIN country co
    ON ci.countrycode = co.code
 WHERE co.continent = 'Asia'