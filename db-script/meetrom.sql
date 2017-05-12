-- =================================================================================
-- 作者：田川
-- 日期：2017-05-07
-- 功能：数据库创建文件
-- 更新：2017-05-08优化数据表注释
-- 备注：无
-- =================================================================================
-- 创建数据库
DROP DATABASE IF EXISTS meetrom;
CREATE DATABASE meetrom character set utf8;
USE meetrom;
SET NAMES 'utf8';
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
    ID  INT(10) AUTO_INCREMENT, -- 自增长标志位
    Adminid  INT(10), -- 管理员ID
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
    UNIQUE(Adminid), -- 唯一约束符
    PRIMARY KEY(ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

-- ===============================================================================
-- 作者：田川
-- 日期：2017-05-06
-- 功能：创建存储会议室信息表
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- ===============================================================================
-- 创建存储会议室信息表
USE meetrom;
DROP TABLE IF EXISTS Conference;
CREATE TABLE Conference (
    ID INT(10) AUTO_INCREMENT, -- 会议室ID
    Sqrzh VARCHAR(40), -- 申请人账号
    Sqrxm VARCHAR(40), -- 申请人姓名
    Name VARCHAR(40) NOT NULL, -- 会议室名
    Didian VARCHAR(40) NOT NULL, -- 会议室地点
    Duomeiti VARCHAR(40) NOT NULL, -- 是否多媒体教室
    Rongnarenshu VARCHAR(40) NOT NULL, -- 容纳人数
    Hueiyizhuti VARCHAR(40), -- 会议主题
    Shenqingzhuangtai VARCHAR(40), -- 申请状态
    Shenpi VARCHAR(40), -- 会议室审批
    Shenqliyou VARCHAR(40), -- 申请理由
    Shenqsjian VARCHAR(40), -- 申请时间
    PRIMARY KEY(ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

-- ===============================================================================
-- 作者：田川
-- 日期：2017-05-06
-- 功能：创建存储管理员上传的照片信息表
-- 更新：2017-04-07优化数据表注释
-- 备注：无
-- ===============================================================================
-- 创建存储管理员上传的照片数据表
USE meetrom;
DROP TABLE IF EXISTS storePicture;
CREATE TABLE storePicture (
    ID  INT(10) AUTO_INCREMENT, -- 自增长标志位
    Adminid  INT(10) , -- 管理员ID
    nameplates VARCHAR(40) NOT NULL, -- 管理员照片
    storePicture VARCHAR(16) NOT NULL, -- 会议室地点
    UNIQUE(Adminid), -- 唯一约束符
    PRIMARY KEY(ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;

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
    PRIMARY KEY(ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
 