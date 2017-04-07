-- ===============================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：创建用户信息数据表
-- 更新：2017-04-07优化数据表注释
-- 备注：时间为追加
-- ===============================================================================
-- 创建用户信息数据表
USE bounty;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	name VARCHAR(255) NOT NULL UNIQUE, -- 用户注册姓名
	pwd VARCHAR(255) NOT NULL, -- 用户注册密码
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 用户注册时间
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
