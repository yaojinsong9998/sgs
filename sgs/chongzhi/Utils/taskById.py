import pyautogui
import time
import pyperclip
import pydirectinput

#任务
from sgs.chongzhi.Utils.input import inputConfig
from sgs.chongzhi.Utils.mouse import mouseClick
from sgs.chongzhi.Utils.processFunction import processFuction


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
            mouseClick(1,"left",img,reTry)
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
            res = mouseClick(1, "left", img, reTry)
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