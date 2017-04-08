-- ===============================================================================
-- 作者：韩望
-- 日期：2017-04-08
-- 功能：创建房产中介信息表
-- 更新：初创，无
-- 备注：初创，无
-- ===============================================================================
-- 创建房产中介信息表
USE bounty;
DROP TABLE IF EXISTS estate_agents;
CREATE TABLE estate_agents (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	name VARCHAR(255) NOT NULL UNIQUE, -- 房产中介名称
	level TINYINT(4) NOT NULL DEFAULT 1, -- 房产中介布局等级信息
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 用户注册时间
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
