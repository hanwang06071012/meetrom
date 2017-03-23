-- ===============================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：创建用户信息数据表
-- 更新：首次创建，无
-- 备注：时间为追加
-- ===============================================================================
USE bounty;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id	INT(10) AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL UNIQUE,
	pwd VARCHAR(255) NOT NULL,
	timecreate TIMESTAMP,
	timemodify DATETIME NULL,
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
