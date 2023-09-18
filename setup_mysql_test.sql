-- script that prepares a MySQL server for the project
-- create a new database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all priviledges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select priviledges to the new user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges to ensure that changes are applied immediately
FLUSH PRIVILEGES;
