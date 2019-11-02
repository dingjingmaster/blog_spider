-- 初始密码
-- use mysql;
-- UPDATE user SET authentication_string='' WHERE User='root';
-- FLUSH PRIVILEGES;
-- ALTER user 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
-- FLUSH PRIVILEGES;

-- 数据库名字 blog_sp
use blog_sp;


-- 文章主要信息
CREATE TABLE IF NOT EXISTS `blog_passage`
(
    `id`        INT PRIMARY KEY AUTO_INCREMENT,         -- id 自增
    `url`       VARCHAR(300) NOT NULL,                  -- 文章url，去重
    `title`     VARCHAR(300) DEFAULT NULL,              -- 文章标题（字符串）
    `data`      INT(12),                                -- 发表/更新日期（20190909）
    `category`  VARCHAR(300) DEFAULT NULL,              -- 分类（字符串）
    `tag`       VARCHAR(300) NOT NULL,                  -- 标签（字符串）
    `spider`    VARCHAR(100) NOT NULL,                  -- 爬虫名字（字符串）
    `content`   TEXT NOT NULL,                          -- 內容（字符串，以HTML或XML 保存）
) DEFAULT CHARSET = utf8;


-- 文章涉及到的图片
CREATE TABLE IF NOT EXISTS `blog_image`
(
    `id`        INT PRIMARY KEY AUTO_INCREMENT,         -- id 自增
    `url`       VARCHAR(300) NOT NULL,                  -- 图片url，去重
    `name`      VARCHAR(300) NOT NULL,                  -- 图片的名字
    `ext_name`  VARCHAR(300) NOT NULL,                  -- 图片扩展名
    `context`   BLOB DEFAULT NULL,                      -- 图片內容
    `pid`       INT(12) NOT NULL,                       -- 图片所属文章 ID
    UNIQUE (`url`)
) DEFAULT CHARSET = utf8;
