import pymysql

#根据账号获取密码
#return : str类型
def selectById(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

#查询最后一个id
def selectLastId():
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

#根据账号获取身份证信息
#return : 元组
def selectCardById(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

#根据账号获取全量信息
#return : 元组
def selectDetailById(id):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select * from usertest where id = '" + id + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception:
        print("selectCardById查询失败")

#根据时间获取账号和密码
#return : [[账号,密码],[账号,密码]]
def selectUserByData(date,line):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select id,password from usertest where date = '" + date + "' and isCost = 0 order by addtime limit " + str(line)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception:
        print("selectUserByData查询失败")

#根据时间获取当日创建账号数量
#return : int
def selectNumByDate(date):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select count(*) from usertest where isCost = 0 and date = '" + date + "'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]
    except Exception:
        print("selectNumByDate查询失败")

#获取指定日期内未浇水账号
#return : [[账号,密码],[账号,密码]]
def selectDailyNum(date):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

#获取2-7天账号
#return : [[账号,密码],[账号,密码]]
def selectNum2To7(date):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

#获取当天注册账号
#return : [[账号,密码],[账号,密码]]
def selectNum2To7(date):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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

def select():
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
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