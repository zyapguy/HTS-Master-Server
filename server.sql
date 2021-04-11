CREATE TABLE `current_active_servers` (
	`server_id` INT(11) NOT NULL AUTO_INCREMENT,
	`server_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`server_ip` VARCHAR(25) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`server_usercount` INT(5) NULL DEFAULT NULL,
	`server_map` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	INDEX `server_id` (`server_id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=5
;
