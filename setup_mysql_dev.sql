-- script that prepares a MySQL server for the project
-- create a new database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all priviledges to the new user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select priviledges to the new user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush privileges to ensure that changes are applied immediately
FLUSH PRIVILEGES;
