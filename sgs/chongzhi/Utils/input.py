import random
import time

from sql.insert import insertNewUser
from sql.select import selectById, selectLastId, selectCardById
from sql.shenfenzheng.select import selectNum, selectByIndex
from sql.update import updateComplete, updateCard


def inputConfig(type,data):
    if type == "dengluzhanghao":
        id = data[0]
        return id
    elif type == "denglumima":
        password = data[1]
        return password
    elif type == "zfbmima":
        return 126288