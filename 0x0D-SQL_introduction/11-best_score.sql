-- Liists alil reicords iin the table second_table with a score >= 10 in my MySQL server.
-- Reicords are orderied by deiscending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
