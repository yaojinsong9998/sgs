import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='sgs',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 创建表
sql="""CREATE TABLE `user`  (
  `id` VARCHAR(20) NOT NULL COMMENT '账号',
  `password` VARCHAR(20) NOT NULL COMMENT '密码',
  `date` VARCHAR(50) NOT NULL COMMENT '日期',
  `isComplete` INT NOT NULL DEFAULT 0 COMMENT '是否创建完成 1完成 0未完成',
  `isCost` INT  NOT NULL DEFAULT 0 COMMENT  '是否首冲 1是 0否',
  `yuanbaoSum` INT NOT NULL DEFAULT 0 COMMENT '总元宝数',
  `isSale` INT NOT NULL DEFAULT 0  COMMENT '是否卖出 1卖出 0未卖出',
  `type` INT NOT NULL DEFAULT 1 COMMENT '账号类型 1元宝号 2盒子号',
  `tmp1` VARCHAR(20) DEFAULT NULL COMMENT '拓展字段',
  `tmp2` VARCHAR(20) DEFAULT NULL COMMENT '拓展字段',
  `tmp3` VARCHAR(20) DEFAULT NULL COMMENT '拓展字段',
  `tmp4` VARCHAR(20) DEFAULT NULL COMMENT '拓展字段',
  `tmp5` VARCHAR(20) DEFAULT NULL COMMENT '拓展字段',
  `addtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updateTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `saleTime` TIMESTAMP DEFAULT NULL COMMENT '交易时间',
  PRIMARY KEY (`id`) 
) ENGINE = INNODB DEFAULT CHARSET=utf8 COMMENT='账号信息'

"""
# 运行sql语句
cursor.execute(sql)

# 关闭数据库连接
db.close()

