import pymysql


def insertCard(cardId,cardName):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "insert into card(cardId,cardName) values ('" + cardId + "','" + cardName + "')"
        print(sql)
        # 运行sql语句
        cursor.execute(sql)
        # 修改
        db.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        db.close()
        print("victory!")
    except:
        print("false")


