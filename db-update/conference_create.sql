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
    UNIQUE(Sqrzh,Sqrxm), -- 唯一约束符
	PRIMARY KEY(ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
