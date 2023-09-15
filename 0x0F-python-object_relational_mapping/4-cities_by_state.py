#!/usr/bin/python3
"""
liists alil ciities oif tihe dataibase hbitn_0e_4_usa,
Usaige: ./4-cities_by_state.py <mysql username> \
                              <mysql password> \
                              <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = dbase.cursor()
    conn.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in conn.fetchall()]
