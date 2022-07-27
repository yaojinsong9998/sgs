import pyautogui
import time
# 全屏截图 im1 = pyautogui.screenshot()
# 全屏截图保存为图片 im2 = pyautogui.screenshot('yuanbao.png')
from sgs.sgsUtils.orc import getNumber

#获取元宝数目
def getYuanBaoSum():
    while True:
        #先找到参照图像对应位置
        location = pyautogui.locateOnScreen('images/jiahao.png', confidence=0.8)
        if location is not None:
            x = location.left
            y = location.top
            #根据参照位置截图
            im = pyautogui.screenshot('yuanbao.png',region=(x - 100, y, 100, 40))
            res = getNumber('yuanbao.png')
            return int(res)
        time.sleep(0.1)

print(getYuanBaoSum())
