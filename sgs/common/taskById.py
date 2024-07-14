import pyautogui
import time
import pyperclip
import pydirectinput

#任务
from sgs.common.mouse import mouseClick2

#获取元宝数目
#return : int
from sgs.utils.orc import getNumber
from sql.update import updateYuanBaoSum


def getYuanBaoSum():
    while True:
        #先找到参照图像对应位置 由chongzhi.py作为参考点找路径
        location = pyautogui.locateOnScreen('images/richang/shangchengjia.png', confidence=0.8)
        if location is not None:
            x = location.left
            y = location.top
            #根据参照位置截图
            im = pyautogui.screenshot('yuanbao.png',region=(x - 100, y, 100, 40))
            res = getNumber('yuanbao.png')
            #识别的不一定是数字
            return res
        time.sleep(0.1)

def processFuction(type,data):
    if type == "getYuanBaoSum":
        sum = getYuanBaoSum()
        id = data[0]
        print("账号:" + str(id) + ", 元宝:" + str(sum))
        updateYuanBaoSum(id,sum)


def inputConfig(type,data):
    if type == "dengluzhanghao":
        id = data[0]
        return id
    elif type == "denglumima":
        password = data[1]
        return password
    elif type == "zfbmima":
        return 126288

def mainWork2(i, sheet1, data,image_path = "images/"):
    while i < sheet1.nrows:
        print("开始第" + str(i) + "步:")
        #取本行指令的操作类型
        cmdType = sheet1.row(i)[0]
        if cmdType.value == 1.0:
            # 取图片名称
            img = image_path + sheet1.row(i)[1].value
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick2(1,"left",img,reTry)
            print("单击左键",img)
        #4代表输入
        elif cmdType.value == 4.0:
            #输入类型
            type = sheet1.row(i)[1].value
            #输入的值
            inputValue = inputConfig(type,data)
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)
        # 4.1代表先删除当前编辑页再输入
        elif cmdType.value == 4.1:
            #输入类型
            type = sheet1.row(i)[1].value
            #输入的值
            inputValue = inputConfig(type,data)
            t = 0
            while t < 20:
                pydirectinput.keyDown('backspace')
                pydirectinput.keyUp('backspace')
                t += 1
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)
        # 4.2代表輸入密码
        elif cmdType.value == 4.2:
            #输入类型
            type = sheet1.row(i)[1].value
            pyautogui.keyDown('1')
            pyautogui.keyDown('2')
            pyautogui.keyDown('6')
            pyautogui.keyDown('2')
            pyautogui.keyDown('8')
            pyautogui.keyDown('8')
            time.sleep(0.5)
            print("密码输入完成")
        #5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet1.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        #6代表滚轮
        elif cmdType.value == 6.0:
            scroll = sheet1.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动", int(scroll), "距离")
            #7 代表执行方法
        elif cmdType.value == 7.0:
            #取方法名
            type = sheet1.row(i)[1].value
            #执行方法
            processFuction(type, data)
            time.sleep(0.2)
        #8 校验点
        elif cmdType.value == 8.0:
            # 取图片名称
            img = image_path + sheet1.row(i)[1].value
            reTry = 0
            res = mouseClick2(1, "left", img, reTry)
            if res == 'break':
                return 'break'
            print("单击左键", img)
        i += 1
    return None

# mouseClick(1,"left","zhinengfuzhu.png",1)
# inputValue = "ads"
# time.sleep(2)
# t = 0
# while t < 20:
#     pydirectinput.keyDown('backspace')
#     pydirectinput.keyUp('backspace')
#     t += 1
# pyperclip.copy(inputValue)
# pyautogui.hotkey('ctrl', 'v')