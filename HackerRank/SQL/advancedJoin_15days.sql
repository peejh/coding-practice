

-- MS SQL Server
-- The first 3 CTEs are for solving who has the most submissions per day
-- The last CTE is for calculating per day the unique submissions since day 1 (2nd col)
-- The 2nd column solution was taken from the MySQL solution below
WITH
submitted AS (
    SELECT submission_date,
           hacker_id,
           COUNT(*) subs
      FROM submissions
     GROUP BY submission_date, hacker_id
),
max_submitted AS (
    SELECT submission_date,
           hacker_id,
           subs,
           MAX(subs) OVER(PARTITION BY submission_date) max_subs
      FROM submitted
),
winners AS (
    SELECT submission_date,
           MIN(hacker_id) win_hacker_id
      FROM max_submitted
     WHERE subs = max_subs
     GROUP BY submission_date
),
unique_subs_from_day_one AS (
    -- think of this as a for each loop
    SELECT DISTINCT submission_date, 
           (
                SELECT COUNT(DISTINCT s2.hacker_id)
                  FROM submissions s2
                 WHERE s2.submission_date = s1.submission_date
                   AND (
                            SELECT COUNT(DISTINCT s3.submission_date)
                              FROM submissions s3
                             WHERE s3.hacker_id = s2.hacker_id
                               AND s3.submission_date < s1.submission_date
                       ) = DATEDIFF(dd, '2016-03-01', s1.submission_date)
           ) unique_sub
      FROM submissions s1
)

SELECT u.submission_date,
       u.unique_sub,
       w.win_hacker_id,
       h.name
  FROM unique_subs_from_day_one u
  JOIN winners w
    ON w.submission_date = u.submission_date
  JOIN hackers h
    ON h.hacker_id = w.win_hacker_id
 ORDER BY submission_date


-- MySQL
-- written by someone else
select submission_date,
    (
        select COUNT(distinct hacker_id)  
        from submissions s2  
        where s2.submission_date = s1.submission_date
            and (
                    select COUNT(distinct s3.submission_date)
                    from submissions s3
                    where s3.hacker_id = s2.hacker_id 
                        and s3.submission_date < s1.submission_date
                ) = DATEDIFF(s1.submission_date , '2016-03-01')
    ),
    (
        select hacker_id
        from submissions s2
        where s2.submission_date = s1.submission_date 
        group by hacker_id
        order by count(submission_id) desc, hacker_id limit 1
    ) as hacker_of_day,
    (
        select name
        from hackers
        where hacker_id = hacker_of_day
    )
from (select distinct submission_date from submissions) s1
group by submission_date