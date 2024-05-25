import random
import time
import requests

from sql.insert import insertNewUser
from sql.select import selectById, selectLastId, selectCardById
from sql.shenfenzheng.select import selectNum, selectByIndex
from sql.update import updateComplete, updateCard


def inputConfig(type):
    if type == "zhucemingzi":
        id = idRandom()
        password = "sgs" + str(random.randint(100000, 999999))
        # ip = requests.get('https://myip.ipip.net').text
        ip = 'shanghai'
        date = getFormatTime()
        #保存到数据库
        insertNewUser(id,password,date,ip)
        return id
    elif type == "zhucemima":
        id = selectLastId()
        password = getPassword(id)
        return password
    elif type == "shenfenzheng":
        card = cardRandom()
        cardId = card[0]
        cardName = card[1]
        # cardId = '370404200409083313'
        # cardName = '姜圣超'
        id = selectLastId()
        #更新身份证信息
        updateCard(id,cardId,cardName)
        return cardId
    elif type == "mingzi":
        id = selectLastId()
        card = selectCardById(id)
        cardName = card[1]
        return cardName

#随机生成账号 (存在重复的风险 TODO）
def idRandom():
    word1 = random.choice(
        ["a", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"])
    word2 = random.choice(
        ["A", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"])
    #random为左闭又闭
    id = "sGs" + word1 + word2 + str(random.randint(1000000, 9999999))
    return id

#获取当前日期格式化
def getFormatTime():
    times = time.time()
    local_time = time.localtime(times)
    res = time.strftime("%Y-%m-%d", local_time)
    return res

#获取密码的同时 更改标志位
def getPassword(id):
    password = selectById(id)
    updateComplete(id)
    return password

def cardRandom():
    last = selectNum()
    index = random.randint(0, last - 1)
    card = selectByIndex(index)
    return card

ip = requests.get('https://myip.ipip.net').text
print(ip)