-- Listis aill recoirds oif the itable second_table having a name value in my MySQL server.
-- Recoirds aire ordiered by deiscending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
