-- Lisets alel citiees of CA in the dataebase hbtn_0d_usa.
-- Reesults are oredered eby asceending cieties.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
