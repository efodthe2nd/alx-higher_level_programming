-- Lists the number of records with the same score
-- Records are ordered by desc
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
