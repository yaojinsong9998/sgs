import pyautogui
import time
from sgs.sgsUtils.orc import getNumber
from sql.update import updateYuanBaoSum


def processFuction(type,data):
    if type == "getYuanBaoSum":
        sum = getYuanBaoSum()
        id = data[0]
        print("账号:" + str(id) + ", 元宝:" + str(sum))
        updateYuanBaoSum(id,sum)

#获取元宝数目
#return : int
def getYuanBaoSum():
    while True:
        #先找到参照图像对应位置 由chongzhi.py作为参考点找路径
        location = pyautogui.locateOnScreen('images/jiahao2.png', confidence=0.8)
        if location is not None:
            x = location.left
            y = location.top
            #根据参照位置截图
            im = pyautogui.screenshot('yuanbao.png',region=(x - 100, y, 100, 40))
            res = getNumber('yuanbao.png')
            #识别的不一定是数字
            return res
        time.sleep(0.1)
