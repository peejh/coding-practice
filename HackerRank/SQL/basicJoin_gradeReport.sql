-- https://www.hackerrank.com/challenges/the-report
-- Difficulty: MEDIUM

SELECT
    CASE WHEN g.grade >= 8
        THEN s.name
        ELSE 'NULL'
    END, 
    g.grade,
    s.marks
FROM students s
INNER JOIN grades g
    ON g.min_mark <= s.marks 
    AND g.max_mark >= s.marks
ORDER BY g.grade DESC,
    CASE WHEN g.grade < 8
        THEN s.marks
        ELSE s.name
    END