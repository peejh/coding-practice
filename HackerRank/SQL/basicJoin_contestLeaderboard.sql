-- https://www.hackerrank.com/challenges/contest-leaderboard
-- Difficulty: MEDIUM

WITH
max_scores AS (
    SELECT hacker_id, challenge_id, MAX(score) max_score
      FROM submissions
     GROUP BY hacker_id, challenge_id
),
total_scores AS (
    SELECT hacker_id, SUM(max_score) total_score
      FROM max_scores
     GROUP BY hacker_id
)
SELECT h.hacker_id, h.name, ts.total_score
  FROM hackers h
 INNER JOIN total_scores ts
    ON h.hacker_id = ts.hacker_id
 WHERE ts.total_score > 0
 ORDER BY ts.total_score DESC, h.hacker_id