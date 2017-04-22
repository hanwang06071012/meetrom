-- ===============================================================================
-- 作者：韩望
-- 日期：2017-04-17
-- 功能：创建资源信息数据表
-- 更新：初创，无
-- 备注：初创，无
-- ===============================================================================
-- 创建资源信息数据表
USE bounty;
DROP TABLE IF EXISTS source;
CREATE TABLE source (
    id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
    name VARCHAR(255) NOT NULL, -- 资源名称
    source_path VARCHAR(255) NULL,
    node_id INT(11) NOT NULL, -- 资源的节点ＩＤ
    parent_id INT(11) NULL, -- 资源的父节点ＩＤ
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 用户注册时间
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
