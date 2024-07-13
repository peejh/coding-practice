-- https://www.hackerrank.com/challenges/the-pads
-- Difficulty: MEDIUM

-- MySQL
SELECT CONCAT(name, '(', SUBSTR(occupation, 1, 1), ')') AS tag
  FROM occupations
 ORDER BY tag;

SELECT CONCAT('There are a total of ', tally, ' ', LOWER(occupation), 's.')
  FROM (
        SELECT occupation, COUNT(*) AS tally
          FROM occupations
         GROUP BY occupation
) tallies
 ORDER BY tally, occupation;