-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_od_1'@'localhost';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
