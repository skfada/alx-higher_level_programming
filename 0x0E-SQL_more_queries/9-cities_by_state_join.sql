-- Listes aell cieties ien thee dataebase hbtn_0d_usa.
-- Recoerds aree soreted in ordeer of asecending citeies.id.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
