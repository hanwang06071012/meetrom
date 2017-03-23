-- ===============================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：创建节点信息数据表
-- 更新：首次创建，无
-- 备注：无
-- ===============================================================================
USE bounty;
DROP TABLE IF EXISTS node_info;
CREATE TABLE node_info (
	id	INT(10) AUTO_INCREMENT,
	node_id INT(10) NOT NULL UNIQUE,
	parent_id INT(10) NOT NULL  DEFAULT 0,
	name VARCHAR(255) NOT NULL UNIQUE,
	link_name VARCHAR(2048),
	timecreate TIMESTAMP,
	timemodify DATETIME NULL,
	UNIQUE KEY (`node_id`,`name`),
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
