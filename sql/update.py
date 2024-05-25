import pymysql

#更新完成位 （密码是否用到）
def updateComplete(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set isComplete = 1 where id = '" + id + "'";
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

#更新完成位 （新手任务是否完成）
def updateFinish(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set isFinish = 1,is_True = 1 where id = '" + id + "'";
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

#更新身份证信息
def updateCard(id,cardId,cardName):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set cardId = '" + cardId + "'," + "cardName = '" + cardName + "' where id = '" + id + "'";
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

#更新完成位 （首冲是否完成）
def updateCost(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set isCost = 1 where id = '" + id + "'";
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

#更新元宝数
def updateYuanBaoSum(id,yuanbaoSum):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        #sql = "update usertest set yuanbaoSum = " + str(yuanbaoSum) + " where id = '" + id + "'";
        sql = "update usertest set yuanbaoSum = '" + yuanbaoSum + "'" + " where id = '" + id + "'";
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

#更新天数
def updateDay(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set day = day + 1 where id = '" + id + "'";
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

#更新天数
def updateStatus(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update usertest set `status` = 2,`check` = `check` + 1 where id = '" + id + "'";
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