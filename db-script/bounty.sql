-- =================================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：数据库创建文件
-- 更新：无
-- 备注：无
-- =================================================================================
-- 创建数据库
DROP DATABASE IF EXISTS bounty;
CREATE DATABASE bounty character set utf8;
USE bounty;
SET NAMES 'utf8';

-- 创建用户信息数据表
USE bounty;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id	INT(10) AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL UNIQUE,
	pwd VARCHAR(255) NOT NULL,
	timecreate TIMESTAMP,
	timemodify DATETIME  NULL ,
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

-- 创建节点信息数据表
USE bounty;
DROP TABLE IF EXISTS node_info;
CREATE TABLE node_info (
	id	INT(10) AUTO_INCREMENT,
	node_id INT(10) NOT NULL UNIQUE,
	parent_id INT(10) NOT NULL  DEFAULT 0,
	name VARCHAR(255) NOT NULL UNIQUE,
	link_name VARCHAR(2048),
	addris BOOL NULL DEFAULT FALSE,
	timecreate TIMESTAMP,
	timemodify DATETIME  NULL,
	UNIQUE KEY (`node_id`,`name`),
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;


