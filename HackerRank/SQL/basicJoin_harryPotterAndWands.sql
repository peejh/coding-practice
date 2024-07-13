-- https://www.hackerrank.com/challenges/harry-potter-and-wands
-- Difficulty: MEDIUM

WITH
power_age_coins AS (
    SELECT w.id, w.power, p.age, w.coins_needed
      FROM wands w
     INNER JOIN wands_property p
        ON w.code = p.code
     WHERE p.is_evil = 0
),
min_coins_per_power_age AS (
    SELECT power, age, MIN(coins_needed) min_coins
      FROM power_age_coins
     GROUP BY power, age
)
SELECT pac.id, pac.age, mc.min_coins, pac.power
  FROM power_age_coins pac
 INNER JOIN min_coins_per_power_age mc
    ON pac.power = mc.power AND pac.age = mc.age
 WHERE pac.coins_needed = mc.min_coins
 ORDER BY pac.power DESC, pac.age DESC