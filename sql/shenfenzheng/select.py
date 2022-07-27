import pymysql

#查指定行的信息
#return [身份证号，姓名]
def selectByIndex(index):
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select * from card where isUse = 1 limit " + str(index) + ",1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception:
        print("selectByIndex查询失败")

#查询数量
#return : int类型
def selectNum():
    db = pymysql.connect(host='localhost',user='root',password='123456',database='sgs',charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 查询语句
    try:
        cursor = db.cursor()
        sql = "select count(*) from card where isUse = 1"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]
    except Exception:
        print("selectNum查询失败")

