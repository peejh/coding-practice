-- https://www.hackerrank.com/challenges/salary-of-employees
-- Difficulty: EASY

SELECT name
  FROM employee
 WHERE salary > 2000
   AND months < 10
 ORDER BY employee_id