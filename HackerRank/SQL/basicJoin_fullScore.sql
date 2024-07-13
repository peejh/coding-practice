-- https://www.hackerrank.com/challenges/full-score
-- Difficulty: MEDIUM

SELECT hacker_id, name
  FROM (
        SELECT h.hacker_id, h.name, COUNT(s.score) completed
          FROM submissions s
         INNER JOIN hackers h    ON s.hacker_id = h.hacker_id
         INNER JOIN challenges c ON s.challenge_id = c.challenge_id
         INNER JOIN difficulty d ON c.difficulty_level = d.difficulty_level
         WHERE s.score = d.score
         GROUP BY s.hacker_id, h.name
) temp
 WHERE completed > 1
 ORDER BY completed DESC, hacker_id