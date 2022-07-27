import pymysql

def delete():
    db = pymysql.connect(host='localhost',user='root', password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 删除语句
    sql = "DELETE FROM usertest WHERE id='ddsAC'"
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 向数据库提交
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()
    # 关闭连接
    db.close()
    # 成功提示
    print("victory!")