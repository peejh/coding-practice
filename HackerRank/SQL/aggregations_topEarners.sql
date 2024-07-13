-- https://www.hackerrank.com/challenges/earnings-of-employees
-- Difficulty: EASY

SELECT (months * salary) AS total_earnings, COUNT(*)
  FROM employee
 GROUP BY total_earnings
 ORDER BY total_earnings DESC
 LIMIT 1