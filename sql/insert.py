import pymysql


def insertNewUser(id,password,date,ip):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "insert into usertest(id,password,date,ip) values ('" + id + "','" + password + "','" + date + "','" +ip + "')"
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


def insert2():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "insert into usertest(id,password,date) values ('3dd','dd','ddd')"
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

def insert3():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "insert into usertest(id,password,date,ip) values ('3ddysAC','dd','ddd','IP：60.190.119.91')"
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

def insert4():
    id = '2223C'
    password = 'dd'
    date = 'ddd'
    ip = 'IP：60.190.119.91'
    db = pymysql.connect(host='localhost', user='root', password='123456', database='sgs', charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "insert into usertest(id,password,date,ip) values ('" + id + "','" + password + "','" + date + "','" + ip + "')"
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

# insert4()