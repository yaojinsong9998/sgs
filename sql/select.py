import pymysql


def excuteSelectSql(sql, resultType='one'):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 查询语句
    try:
        cursor = db.cursor()
        print(sql)
        cursor.execute(sql)
        if resultType == 'one':
            return cursor.fetchone()
        if resultType == "all":
            return cursor.fetchall()
    except Exception:
        print("selectById查询失败")


# 根据账号获取密码
# return : str类型
def selectById(id):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select password from usertest where id = '" + id + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]
    except Exception:
        print("selectById查询失败")


# 查询最后一个id
def selectLastId():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select id from usertest order by addtime desc limit 1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]
    except Exception:
        print("查询失败")


# 根据账号获取身份证信息
# return : 元组
def selectCardById(id):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select cardId,cardName from usertest where id = '" + id + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception:
        print("selectCardById查询失败")


# 根据账号获取全量信息
# return : 元组
def selectDetailById(id):
    sql = f"select * from usertest where id = '{id}'".format(id)
    result = excuteSelectSql(sql)
    return result


# 根据时间获取账号和密码
# return : [[账号,密码],[账号,密码]]
def selectUserByData(date, line):
    sql = f"select id,password from usertest where date = '{date}' and isCost = 0 " \
          f"order by addtime limit {line}".format(date,line)
    result = excuteSelectSql(sql,"all")
    return result


# print(selectUserByData('2022-07-27',10))

# 根据时间获取当日创建账号数量
# return : int
def selectNumByDate(date):
    sql = f"select count(*) from usertest where isCost = 0 and date = '{date}'".format(date)
    result = excuteSelectSql(sql)
    return result[0]


# 获取指定日期内未浇水账号
# return : [[账号,密码],[账号,密码]]
def selectDailyNum(date):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select id,password from usertest where day > 7 and updateTime < '" + date + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectDailyNum查询失败")


# #获取指定账号
# #return : [[账号,密码],[账号,密码]]
# def selectById(id):
#     db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 查询语句
#     try:
#         cursor = db.cursor()
#         sql = "select id,password from usertest where id = '" + id + "'"
#         print(sql)
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         return result
#     except Exception:
#         print("selectDailyNum查询失败")

# 获取2-7天账号
# return : [[账号,密码],[账号,密码]]
def selectNum2To7(date):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select id,password from usertest where day > 1 and day < 7 and updateTime < '" + date + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectNum2To7查询失败")


# 获取当天注册账号
# return : [[账号,密码],[账号,密码]]
def selectNum2To7(date):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select id,password from usertest where day >= 1 and day < 7 and updateTime < '" + date + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectNum2To7查询失败")


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def selectByDate(date, day):
    if date:
        sql = "select id,password from usertest " \
              "where is_delete is null and `status` is null and day = 0 " \
              "and isFinish = 1 and date = '{date}".format(date)
    else:
        sql = f"select id,password from usertest " \
              f"where is_delete is null and `status` is null and day = {day} " \
              f"and isFinish = 1".format(day)
    result = excuteSelectSql(sql, "all")
    return result


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def selectYjs(date, day):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        # if date:
        #     sql = "select id,password from usertest where is_delete is null and `status` is null and day = 7 and isFinish = 1 and date = '" + date + "'"
        # else:
        # sql = f"select id,password from usertest " \
        #       f"where is_delete is null and `status` is null and day = {day} " \
        #       f"and isFinish = 1".format(day)
        if day < 7:
            sql = f"select id,password from usertest " \
                  f"where is_delete is null and `status` is null and day = {day} and day < 7 " \
                  f"and isFinish = 1 and ((cardName = '姚劲嵩' or cardName = '王中云' or cardName = '姚纯洲' or cardName = '姜圣超')  or is_True=1)and updateTime < '{date}'" \
                .format(day, date)
        else:
            sql = f"select id,password from usertest " \
                  f"where is_delete is null and `status` is null and day >= {day} " \
                  f"and isFinish = 1 and ((cardName = '姚劲嵩' or cardName = '王中云' or cardName = '姚纯洲' or cardName = '姜圣超')  or is_True=1)and updateTime < '{date}'" \
                .format(day, date)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectByDate查询失败")


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def selectFirstYjs(date, day):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        start = date + ' 00:00:00'
        end = date + ' 23:59:59'
        cursor = db.cursor()
        sql = f"select id,password from usertest " \
              f"where is_delete is null and `status` is null " \
              f"and isFinish = 1  and addTime > '{start}' and addTime < '{end}'" \
              f"and yuanbaoSum is null" \
            .format(start, end)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectByDate查询失败")


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def checkZhanghao(date):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        if date:
            sql = "select id,password from usertest where `status` is null and day = 2 and isFinish = 1 and date = '" + date + "'"
        else:
            sql = "select id,password from usertest where `status` = 2 and isFinish = 1 and updateTime < '2024-03-17'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectByDate查询失败")


def select():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select password from usertest"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(type(data))
            print(data)
            print(data[0])
    except Exception:
        print("查询失败")
