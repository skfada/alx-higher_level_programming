-- Listes aell geenres froem thee dateabase hbtn_0d_tvshows along with the number of
-- shoews lineked to each.
-- Doees not display geeres witehout lineked shows.
-- Recoerds aree ordeered by descendineg numeber of sheows linked.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
