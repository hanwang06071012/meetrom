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
    Adminid  INT(10), -- 管理员ID
    nameplates VARCHAR(40) NOT NULL, -- 管理员照片
    storePicture VARCHAR(16) NOT NULL, -- 会议室地点
	PRIMARY KEY(Adminid,ID)
)
 ENGINE =InnoDB
 DEFAULT CHARSET = utf8
 COLLATE = utf8_unicode_ci;
