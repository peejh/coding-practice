-- https://www.hackerrank.com/challenges/occupations
-- Difficulty: MEDIUM

-- MS SQL Server
-- Only works because we know that `professors` has the
-- most members
WITH
professors AS(
    SELECT ROW_NUMBER() OVER(ORDER BY name) rownum, name
      FROM occupations
     WHERE occupation = 'Professor'
),
doctors AS(
    SELECT ROW_NUMBER() OVER(ORDER BY name) rownum, name
      FROM occupations
     WHERE occupation = 'Doctor'
),
actors AS(
    SELECT ROW_NUMBER() OVER(ORDER BY name) rownum, name
      FROM occupations
     WHERE occupation = 'Actor'
),
singers AS(
    SELECT ROW_NUMBER() OVER(ORDER BY name) rownum, name
      FROM occupations
     WHERE occupation = 'Singer'
)

SELECT d.name Doctor, p.name Professor, s.name Singer, a.name Actor
  FROM professors p
  FULL OUTER JOIN doctors d
    ON p.rownum = d.rownum
  FULL OUTER JOIN singers s
    ON p.rownum = s.rownum
  FULL OUTER JOIN actors a
    ON p.rownum = a.rownum


-- MS SQL Server 
WITH
orderedOccupations AS (
    SELECT
           ROW_NUMBER() OVER(PARTITION BY occupation ORDER BY name) rownum,
           name,
           occupation
      FROM occupations
)

SELECT
       MIN(CASE WHEN occupation = 'Doctor' THEN name END) AS Doctor,
       MAX(CASE WHEN occupation = 'Professor' THEN name END) AS Professor,
       MIN(CASE WHEN occupation = 'Singer' THEN name END) AS Singer,
       MAX(CASE WHEN occupation = 'Actor' THEN name END) AS Actor
  FROM orderedOccupations
 GROUP BY rownum