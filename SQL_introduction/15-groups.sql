-- This script displays the number records with the same score
SELECT score, COUNT(*) AS number_of_records
FROM second_table
GROUP BY score;
