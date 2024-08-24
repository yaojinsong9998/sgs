import pymysql


def excuteUpdateSql(sql):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
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


# 更新完成位 （密码是否用到）
def updateComplete(id):
    sql = f"update usertest set isComplete = 1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)


# 更新完成位 （新手任务是否完成）
def updateFinish(id):
    sql = f"update usertest set isFinish = 1,is_True = 1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)

# 更新完成位 （新手任务是否完成）
def updateFinishByPhone(id):
    sql = f"update usertest set isFinish = 1,is_True = 1,is_Phone=1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)


# 更新身份证信息
def updateCard(id, cardId, cardName):
    sql = f"update usertest set cardId = '{cardId}', cardName = '{cardName}' " \
          f"where id = '{id}'".format(cardId, cardName, id);
    excuteUpdateSql(sql)


# 更新完成位 （首冲是否完成）
def updateCost(id):
    sql = f"update usertest set isCost = 1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)


# 更新天数
def updateDay(id):
    sql = f"update usertest set day = day + 1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)


# 更新元宝数
def updateYuanBaoSum(id, yuanbaoSum):
    sql = f"update usertest set yuanbaoSum = '{yuanbaoSum}' " \
          f"where id = '{id}'".format(yuanbaoSum, id);
    excuteUpdateSql(sql)


# 更新天数
def updateStatus(id):
    sql = f"update usertest set `status` = 2,`check` = `check` + 1 where id = '{id}'".format(id)
    excuteUpdateSql(sql)

# 更新活动标志位
def updateHuoDong(id):
    sql = f"update usertest set huodong = 1 where id = '{id}'".format(id);
    excuteUpdateSql(sql)