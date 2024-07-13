
-- MS SQL Server
-- long but it works
WITH
views AS (
    SELECT challenge_id,
           SUM(total_views) total,
           SUM(total_unique_views) uniq
      FROM view_stats
     GROUP BY challenge_id
),
submissions AS (
    SELECT challenge_id,
           SUM(total_submissions) total,
           SUM(total_accepted_submissions) accepted
      FROM submission_stats
     GROUP BY challenge_id
),
college_stats AS (
    SELECT ch.college_id,
           SUM(ss.total) ss_total,
           SUM(ss.accepted) ss_accepted,
           SUM(vs.total) vs_total,
           SUM(vs.uniq) vs_unique
      FROM challenges ch
      LEFT JOIN views vs
        ON vs.challenge_id = ch.challenge_id
      LEFT JOIN submissions ss
        ON ss.challenge_id = ch.challenge_id
     GROUP BY ch.college_id
)

SELECT co.contest_id,
       co.hacker_id,
       co.name, 
       SUM(ss_total),
       SUM(ss_accepted),
       SUM(vs_total),
       SUM(vs_unique)
  FROM college_stats cs
  JOIN colleges cl
    ON cl.college_id = cs.college_id
  JOIN contests co
    ON co.contest_id = cl.contest_id
 GROUP BY co.contest_id, co.hacker_id, co.name
HAVING SUM(ss_total) != 0
    OR SUM(ss_accepted) != 0
    OR SUM(vs_total) != 0
    OR SUM(vs_unique) != 0
 ORDER BY co.contest_id;


--  MS SQL Server
-- a little shorter
WITH
views AS (
    SELECT challenge_id,
           SUM(total_views) vs_total,
           SUM(total_unique_views) vs_unique
      FROM view_stats
     GROUP BY challenge_id
),
submissions AS (
    SELECT challenge_id,
           SUM(total_submissions) ss_total,
           SUM(total_accepted_submissions) ss_accepted
      FROM submission_stats
     GROUP BY challenge_id
)

SELECT co.contest_id,
       co.hacker_id,
       co.name,
       SUM(ss_total),
       SUM(ss_accepted),
       SUM(vs_total),
       SUM(vs_unique)
  FROM contests co
  JOIN colleges cl
    ON co.contest_id = cl.contest_id
  JOIN challenges ch
    ON cl.college_id = ch.college_id
  LEFT JOIN views vs
    ON vs.challenge_id = ch.challenge_id
  LEFT JOIN submissions ss
    ON ss.challenge_id = ch.challenge_id
 GROUP BY co.contest_id, co.hacker_id, co.name
HAVING SUM(ss_total) !=0
    OR SUM(ss_accepted) != 0
    OR SUM(vs_total) != 0
    OR SUM(vs_unique) != 0
 ORDER BY co.contest_id