CREATE TABLE `demo`(
    `id` INT(11) AUTO_INCREMENT,
    `uid` BIGINT(20) NOT NULL DEFAULT 0 COMMENT 'user id in system, unique',
    `name` VARCHAR(16) NOT NULL DEFAULT '' COMMENT 'name',
    `age` SMALLINT(6) NOT NULL DEFAULT 0 COMMENT 'age',
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'time created',
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'time updated',
    PRIMARY KEY (`id`),
    UNIQUE KEY `uniq_uid` (`uid`),
    KEY `idx_updated_at` (`updated_at`)
)ENGINE=INNODB AUTO_INCREMENT=1 CHARSET='utf8mb4' COMMENT='demo';