-- A script that creates a table users
-- id, email and name attributes
CREATE TABLE IF NOT EXISTS users (
	`id` INT NOT NULL AUTO_INCREMENT,
	`email` VARCHAR(255) UNIQUE NOT NULL,
	`name` VARCHAR(255),
	PRIMARY KEY (`id`)
);
