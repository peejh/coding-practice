-- https://www.hackerrank.com/challenges/print-prime-numbers
-- Difficulty: HARD

-- MySQL
-- Solution taken from https://www.geeksforgeeks.org/stored-procedure-for-prime-numbers-in-mysql
DELIMITER $$
CREATE PROCEDURE PRIMES(IN n INT, OUT result VARCHAR(1000))
BEGIN
    DECLARE j, i, flag INT; /* DECLARE VARIABLES */
    SET j := 2;
    SET result := ' ';

    WHILE (j <= n) DO /* LOOP FROM 2 TO n */
        SET i := 2;
        SET flag := 0;

        WHILE (i <= j) DO /* LOOP FROM 2 TO j */
            IF (j % i = 0) THEN
                SET flag := flag + 1;
            END IF;

            SET i := i + 1; /* INCREMENT i */
        END WHILE;

        IF (flag = 1) THEN
            SET result := CONCAT(result, j, '&'); 
        END IF ;

        SET j := j + 1; /* INCREMENT j */
    END WHILE;
END
$$

CALL primes(1000, @result);
SELECT SUBSTR(@result, 1, LENGTH(@result) - 1);

-- MS SQL Server
-- Solution by someone else
WITH NUMS(num) AS (
    SELECT 2
    UNION ALL
    SELECT num + 1 FROM NUMS
    WHERE num < 1000
)
SELECT STRING_AGG(num, '&')
FROM (
    SELECT n1.num
    FROM NUMS n1, NUMS n2
    WHERE n2.num <= n1.num
    GROUP BY n1.num
    HAVING SUM(IIF(n1.num % n2.num = 0, 1, 0)) = 1
) prime
OPTION (MAXRECURSION 0)