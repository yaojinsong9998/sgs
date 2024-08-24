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
    sql = f"select password from usertest where id = '{id}'".format(id)
    result = excuteSelectSql(sql)
    return result[0]



# 查询最后一个id
def selectLastId():
    sql = "select id from usertest order by addtime desc limit 1"
    result = excuteSelectSql(sql)
    return result[0]


# 根据账号获取身份证信息
# return : 元组
def selectCardById(id):
    sql = f"select cardId,cardName from usertest where id = '{id}'".format(id)
    result = excuteSelectSql(sql)
    return result


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
          f"order by addtime limit {line}".format(date, line)
    result = excuteSelectSql(sql, "all")
    return result


# 根据时间获取当日创建账号数量
# return : int
def selectNumByDate(date):
    sql = f"select count(*) from usertest where isCost = 0 and date = '{date}'".format(date)
    result = excuteSelectSql(sql)
    return result[0]


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def selectByDate(date, day):
    if date:
        sql = f"select id,password from usertest " \
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
    result = excuteSelectSql(sql, "all")
    return result

def selectYjs2(date, day):
    sql = f"select id,password from usertest " \
          f"where is_delete is null and `status` is null and day >= {day} and day < 30 " \
          f"and isFinish = 1 and ((cardName = '姚劲嵩' or cardName = '王中云' or cardName = '姚纯洲' or cardName = '姜圣超')  or is_True=1)and updateTime < '{date}'" \
        .format(day, date)
    result = excuteSelectSql(sql, "all")
    return result


# 获取指定天注册有效账号
# return : [[账号,密码],[账号,密码]]
def selectFirstYjs(date):
    start = date + ' 00:00:00'
    end = date + ' 23:59:59'
    sql = f"select id,password from usertest " \
          f"where is_delete is null and `status` is null " \
          f"and isFinish = 1  and addTime > '{start}' and addTime < '{end}'" \
          f"and yuanbaoSum is null" \
        .format(start, end)
    result = excuteSelectSql(sql, "all")
    return result


# 获取未完成活动的账号
def selectHuoDong():
    sql = f"select id,password from usertest where huodong = 0 and updateTime > '2024-07-17 00:00:00'"
    result = excuteSelectSql(sql, "all")
    return result

def selectDaochu(sql):
    result = excuteSelectSql(sql, "all")
    return result