-- https://www.hackerrank.com/challenges/binary-search-tree-1
-- Difficulty: MEDIUM

-- Solution 1
WITH
root AS (
    SELECT n AS node
      FROM bst
     WHERE p IS NULL
),
parent AS (
    SELECT p AS node
      FROM bst
     WHERE p NOT IN (SELECT node FROM root)
     GROUP BY p
),
leaf AS (
    SELECT n AS node
      FROM bst
     WHERE n NOT IN(SELECT * FROM parent)
       AND n NOT IN(SELECT * FROM root)
)

SELECT node, 'Root' AS type
  FROM root
 UNION ALL
SELECT node, 'Inner' AS type
  FROM parent
 UNION ALL
SELECT node, 'Leaf' AS type
  FROM leaf
 ORDER BY node;


-- Solution 2
SELECT
       n AS node,
       CASE
          WHEN p IS NULL THEN 'Root'
          WHEN n IN(SELECT DISTINCT p FROM bst) THEN 'Inner'
          ELSE 'Leaf'
       END AS type
  FROM bst
 ORDER BY node