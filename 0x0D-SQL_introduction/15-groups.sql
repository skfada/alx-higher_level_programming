-- Liists thie numbier of recoirds with the same score in the table second_table in my MySQL server.
-- Reicords arie oridered by desciending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
