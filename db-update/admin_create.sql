-- ===============================================================================
-- 作者：田川
-- 日期：2017-05-06
-- 功能：创建管理员登陆时信息的验证功能和存储管理员个人信息表
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- ===============================================================================
-- 创建管理员登陆时信息的验证功能和存储管理员个人信息表
USE meetrom;
DROP TABLE IF EXISTS Admin;
CREATE TABLE Admin (
    Adminid  INT(10) AUTO_INCREMENT, -- 管理员ID
    AdminName VARCHAR(40) NOT NULL, -- 管理员姓名
    AdminPass VARCHAR(40) NOT NULL, -- 密码
    AdminRepass VARCHAR(40) NOT NULL, -- 确认用户密码
    AdminPassQuestion VARCHAR(40), -- 密码保护问题
    AdminPassReply VARCHAR(40), -- 密码问题的答案
    AdminTrueName VARCHAR(40) NOT NULL, -- 管理员真实姓名
    AdminAddress VARCHAR(100) NOT NULL, -- 管理员联系地址
    AdminEmail VARCHAR(100) NOT NULL, -- 管理员邮件
    AdminSpecialty VARCHAR(40), -- 专业名称
    AdminHuji VARCHAR(40), -- 户 籍
    AdminIDcard VARCHAR(40), -- 身份证
    AdminCsrq VARCHAR(40), -- 出生日期
    AdminJiguan VARCHAR(40), -- 籍 贯
    AdminAge VARCHAR(40), -- 管理员年龄
    AdminSex VARCHAR(40), -- 管理员性别
    AdminPhone VARCHAR(100) NOT NULL, -- 联系电话
	PRIMARY KEY(Adminid)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
