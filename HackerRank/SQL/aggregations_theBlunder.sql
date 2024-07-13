-- https://www.hackerrank.com/challenges/the-blunder
-- Difficulty: EASY

SELECT CEIL(AVG(salary) - AVG(CAST(REPLACE(salary, '0', '') AS DECIMAL)))
FROM employees