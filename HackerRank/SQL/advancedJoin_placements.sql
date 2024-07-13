-- https://www.hackerrank.com/challenges/placements
-- Difficulty: MEDIUM

-- MS SQL Server
WITH
salaries AS (
    SELECT f.id, s.name, me.salary my_salary, bff.salary bff_salary
      FROM friends f
      JOIN packages me
        ON f.id = me.id
      JOIN packages bff
        ON f.friend_id = bff.id
      JOIN students s
        ON f.id = s.id
)

SELECT name
  FROM salaries
 WHERE bff_salary > my_salary
 ORDER BY bff_salary