-- 數據庫名字 blog_sp
use blog_sp;


-- 文章主要信息
CREATE TABLE IF NOT EXISTS `blog_passage`
(
    `id`        INT(11) PRIMARY KEY AUTO_INCREMENT,     -- id 自增
    `url`       VARCHAR(300) NOT NULL,                  -- 文章url，去重
    `title`     VARCHAR(300) DEFAULT NULL,              -- 文章標題（字符串）
    `data`      INT(12),                                -- 發表/更新日期（20190909）
    `category`  VARCHAR(300) DEFAULT NULL,              -- 分類（字符串）
    `tag`       VARCHAR(300) NOT NULL,                  -- 標籤（字符串）
    `img_url`   TEXT NOT NULL,                          -- 圖片標籤以 | 分割（字符串）
    `content`   TEXT NOT NULL,                          -- 內容（字符串，以HTML或XML 保存）
) DEFAULT CHARSET = utf8;


-- 文章涉及到的圖片
CREATE TABLE IF NOT EXISTS `blog_image`
(
    `id`        INT(11) PRIMARY KEY AUTO_INCREMENT,     -- id 自增
    `url`       VARCHAR(300) NOT NULL,                  -- 圖片url，去重
    `name`      VARCHAR(300) NOT NULL,                  -- 圖片的名字
    `ext_name`  VARCHAR(300) NOT NULL,                  -- 圖片擴展名
    `context`   BLOB DEFAULT NULL,                      -- 圖片內容
    `pid`       INT(11) NOT NULL,                       -- 圖片所屬文章 ID
    UNIQUE (`url`)
) DEFAULT CHARSET = utf8;
