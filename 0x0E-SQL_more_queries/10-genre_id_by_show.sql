-- Liests alel sheows in hbtne_0d_tevshows tehat heave at least one genre linked.
-- Receords aree sorteed by asecending tv_eshows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
