-- ===============================================================================
-- 作者：田川
-- 日期：2017-05-06
-- 功能：创建普通用户类别信息的存储信息表
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- ===============================================================================
-- 创建普通用户类别信息的存储信息表
USE meetrom;
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    ID INT(10) AUTO_INCREMENT, -- 自增长标志位
    usersid INT(10), -- 用户ID
    usersName VARCHAR(40) NOT NULL, -- 用户名
    usersPass VARCHAR(40) NOT NULL, -- 用户登录密码
    usersRepass VARCHAR(40) NOT NULL, -- 确认用户密码
    usersPassQuestion VARCHAR(40), -- 密码保护问题
    usersPassReply VARCHAR(40), -- 密码答案
    usersTrueName VARCHAR(40) NOT NULL, -- 用户真实姓名
    usersAddress VARCHAR(100) NOT NULL, -- 用户联系地址
    usersEmail  VARCHAR(100) NOT NULL, -- 用户邮件
    usersSpecialty VARCHAR(40), -- 专业名称
    usersHuji VARCHAR(40), -- 户 籍
    usersIDcard VARCHAR(40), -- 身份证
    usersCsrq VARCHAR(40), -- 出生日期
    usersJiguan VARCHAR(40), -- 籍 贯
    usersAge VARCHAR(40), -- 用户年龄
    usersSex VARCHAR(40), -- 用户性别
    createDate datetime, -- 创建日期
    usersPhone VARCHAR(100) NOT NULL, -- 用户联系电话
    UNIQUE(usersid), -- 唯一约束符
	PRIMARY KEY(usersid,ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
