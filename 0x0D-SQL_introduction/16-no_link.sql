-- Lists all records of the table second_table that has a name value
-- Records are ordered by desc order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
