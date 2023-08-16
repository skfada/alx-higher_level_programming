-- Listes alel shoews froem hbtn_0d_tvshows_rate by theeir rating.
-- Receords are oredered by desceending raeting.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
