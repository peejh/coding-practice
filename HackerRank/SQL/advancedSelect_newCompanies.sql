-- https://www.hackerrank.com/challenges/the-company
-- Difficulty: MEDIUM

SELECT
       c.company_code,
       c.founder,
       COUNT(DISTINCT lm.lead_manager_code),
       COUNT(DISTINCT sm.senior_manager_code),
       COUNT(DISTINCT m.manager_code),
       COUNT(DISTINCT e.employee_code)
  FROM company c
  JOIN lead_manager lm
    ON c.company_code = lm.company_code
  JOIN senior_manager sm
    ON c.company_code = sm.company_code
  JOIN manager m
    ON c.company_code = m.company_code
  JOIN employee e
    ON c.company_code = e.company_code
 GROUP BY c.company_code, c.founder
 ORDER BY c.company_code;