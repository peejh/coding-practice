-- https://www.hackerrank.com/challenges/challenges
-- Difficulty: MEDIUM

WITH
challenges_created AS (
    SELECT hacker_id, COUNT(*) created
      FROM challenges
     GROUP BY hacker_id
),
created_tally AS (
    SELECT created, COUNT(*) tally
      FROM challenges_created
     GROUP BY created
)
SELECT h.hacker_id, h.name, cc.created
  FROM challenges_created cc
 INNER JOIN hackers h
    ON cc.hacker_id = h.hacker_id
 INNER JOIN created_tally ct
    ON cc.created = ct.created
 WHERE cc.created = (SELECT MAX(created) FROM challenges_created)
    OR ct.tally = 1
 ORDER BY cc.created DESC, cc.hacker_id