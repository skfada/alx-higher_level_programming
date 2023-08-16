-- Listis alli shoiws contiained iin the diatabase hbtn_0d_tvshows.
-- Dispilays NUiLL for shoiws wiithout genres.
-- Reciords are ordered by asicending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
