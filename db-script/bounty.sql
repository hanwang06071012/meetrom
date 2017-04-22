-- =================================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：数据库创建文件
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- =================================================================================
-- 创建数据库
DROP DATABASE IF EXISTS bounty;
CREATE DATABASE bounty character set utf8;
USE bounty;
SET NAMES 'utf8';

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

-- ===============================================================================
-- 作者：韩望
-- 日期：2017-03-23
-- 功能：创建节点信息数据表
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- ===============================================================================
-- 创建节点信息数据表
USE bounty;
DROP TABLE IF EXISTS node_info;
CREATE TABLE node_info (
	id	INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
	node_id INT(10) NOT NULL UNIQUE, -- 地址节点信息
	parent_id INT(10) NOT NULL  DEFAULT 0, -- 地址父节点信息
	name VARCHAR(255) NOT NULL UNIQUE, -- 地址名称
	link_name VARCHAR(2048), -- 地址链接名
	addris BOOL NULL DEFAULT FALSE, -- 地址差别标志
	category TINYINT(4)  NOT NULL DEFAULT 3, -- 城市级别，1:一线城市，2:二线城市，3:三线城市，4:四线城市，默认为三线城市
	time_modify TIMESTAMP, -- 自动更新时间
	time_create DATETIME NULL, -- 地址创建时间
	UNIQUE KEY (`node_id`,`name`), -- 地址与节点编号唯一对应
	PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

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

-- ===============================================================================
-- 作者：韩望
-- 日期：2017-04-10
-- 功能：创建房产出租信息表
-- 更新：初创，无
-- 备注：初创，无
-- ===============================================================================
-- 创建房产出租信息表
USE bounty;
DROP TABLE IF EXISTS estate_rental;
CREATE TABLE estate_rental (
    id  INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
    name VARCHAR(255) NOT NULL UNIQUE, -- 房产名称
    node_id INT(10) NOT NULL UNIQUE, -- 地址节点信息
    parent_id INT(10) NOT NULL  DEFAULT 0, -- 地址父节点信息
    rental_manner TINYINT(4) NOT NULL DEFAULT 0, -- 出租方式,1:整套出租,2:单间出租,3:床位出租
    identity TINYINT(4) NOT NULL DEFAULT 0, -- 身份,0:个人转让,1:商家转让
    cell_name VARCHAR(128)  NULL, --  小区名称
    bed_room TINYINT(4)  NULL, -- 卧室数量(个)
    living_room TINYINT(4)  NULL, -- 客厅数量(个)
    bath_room  TINYINT(4)  NULL, -- 卫生间数量(个)
    area  TINYINT(4)  NULL, -- 总体使用面积(平方米)
    total_floor  TINYINT(4)  NULL, -- 楼层总数
    current_floor  TINYINT(4)  NULL, -- 当前楼层数
    room_direction TINYINT(4) NOT NULL DEFAULT 0, -- 房屋朝向,1:东,2:南,3:西,4:北,5:南北,6:东西,7:东南,8:东北,9:西南,10:西北
    decoration_situation TINYINT(4) NOT NULL DEFAULT 1, -- 装修情况,1:毛坯,2:简单装修,3:中等装修,4:精装修,5:豪华装修
    residential_type TINYINT(4) NOT NULL DEFAULT 1, -- 住宅类型,0:普通住宅.1:商用住宅.2:公寓,3:平房,4:别墅,5:其他,6:新里洋房,7:老公房
    housing_configuration  VARCHAR(128) NULL, -- 房屋配置,1:床,2:衣柜,3:沙发,4:电视,5:冰箱,6:洗衣机,7:空调,8:热水器,9:宽带,10:暖气,11:可做饭,12:独立卫生间,13:阳台
    rent INT(10) NOT NULL DEFAULT 0, -- 租金
    payment_method TINYINT(4)  NOT NULL DEFAULT 0, -- 付款方式
    title VARCHAR(128) NOT NULL DEFAULT " null ", -- 发布帖子的标题
    remarks VARCHAR(256) NULL, -- 备注
    image_location VARCHAR(1024) NULL, -- 资料图位置
    contact_person VARCHAR(16) NOT NULL, -- 联系人
    contact_number VARCHAR(64) NOT NULL, --  联系电话
    qq_number VARCHAR(16) NOT NULL, -- QQ号码
    time_modify TIMESTAMP, -- 自动更新时间
    time_create DATETIME NULL, -- 用户注册时间
    set_privacy_protection BOOLEAN NOT NULL DEFAULT 0, -- 设置隐私保护,1:是,0:否
    PRIMARY KEY(id)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

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
    id  INT(10) AUTO_INCREMENT, -- 自动增长记录索引标志
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

