-- ===============================================================================
-- 作者：韩望
-- 日期：2017-04-08
-- 功能：创建城市等级收入信息表
-- 更新：初创，无
-- 备注：初创，无
-- ===============================================================================
-- 创建城市等级收入信息表
USE bounty;
DROP TABLE IF EXISTS income;
CREATE TABLE income (
    id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
    city_type TINYINT(4) NULL, -- 城市等级
    frist_level VARCHAR(32) NULL, -- 第一收入层次
    second_level VARCHAR(32) NULL, -- 第二收入层次
    thrid_level VARCHAR(32) NULL, -- 第三收入层次
    forth_level VARCHAR(32) NULL, -- 第四收入层次
    fifth_level VARCHAR(32) NULL, -- 第五收入层次
    sixth_level VARCHAR(32) NULL, -- 第六收入层次
    seventh_level VARCHAR(32) NULL, -- 第七收入层次
    eigth_level VARCHAR(32) NULL, -- 第八收入层次
    time_modify TIMESTAMP, -- 自动更新时间
    time_create DATETIME NULL, -- 用户注册时间
    PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
