-- https://www.hackerrank.com/challenges/symmetric-pairs
-- Difficulty: MEDIUM

-- MS SQL Server
-- bad version
WITH
equalPairs AS ( -- pairs that have the same value
    SELECT x, y
      FROM functions
     WHERE x = y
     GROUP BY x, y HAVING COUNT(*) > 1
),
nonEqualPairs AS ( -- pairs with different x & y
    SELECT x1 x, y1 y
      FROM (
           SELECT a.x x1, a.y y1, b.x x2, b.y y2
             FROM functions a
             JOIN functions b
               ON a.x = b.y
              AND a.y = b.x
            WHERE a.x <> a.y
    ) temp
     WHERE x1 <= y1
)

SELECT *
  FROM equalPairs
 UNION ALL
SELECT *
  FROM nonEqualPairs
 ORDER BY x


-- MS SQL Server
-- good version
WITH
ordered AS ( -- using row numbers ordered by `x` is useful here
    SELECT x, y, ROW_NUMBER() OVER(ORDER BY x) rownum
      FROM functions
)

SELECT a.x, a.y
  FROM ordered a
  JOIN ordered b
    ON a.x = b.y
   AND a.y = b.x
 WHERE a.rownum <> b.rownum -- eliminates JOINs with self
   AND a.rownum < b.rownum -- gives pairs where x < y and eliminates duplication from pairs where x1 = y1 = x2 = y2
 ORDER BY a.x