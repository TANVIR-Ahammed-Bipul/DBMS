CREATE DATABASE datavault_db;
SHOW GRANTS FOR 'root'@'localhost';
GRANT ALL PRIVILEGES ON datavault_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'datavault_user'@'localhost' IDENTIFIED BY '30657@datavault';
GRANT ALL PRIVILEGES ON datavault_db.* TO 'datavault_user'@'localhost';
FLUSH PRIVILEGES;

USE datavault_db;
SHOW TABLES;

