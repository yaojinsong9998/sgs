import pyautogui
import time
import xlrd
import pyperclip

from sgs.common.input import inputConfig
from sgs.common.judge import judge
from sgs.common.mouse import mouseClick
#任务

def mainWork(i,sheet1,map,num,target):
    while i < sheet1.nrows:
        print("注册进度:" + str(num) + "/" + str(target) + "开始第" + str(i) + "步:")
        #取本行指令的操作类型
        cmdType = sheet1.row(i)[0]
        if cmdType.value == 1.0:
            #取图片名称
            img = "images/" +sheet1.row(i)[1].value
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(1,"left",img,reTry,map)
            print("单击左键",img)
        #2代表双击左键
        elif cmdType.value == 2.0:
            #取图片名称
            img = sheet1.row(i)[1].value
            #取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(2,"left",img,reTry,map)
            print("双击左键",img)
        #3代表右键
        elif cmdType.value == 3.0:
            #取图片名称
            img = sheet1.row(i)[1].value
            #取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(1,"right",img,reTry,map)
            print("右键",img)
        #4代表输入
        elif cmdType.value == 4.0:
            #输入类型
            type = sheet1.row(i)[1].value
            #输入的值
            inputValue = inputConfig(type)
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)
        # 4.1代表先删除当前编辑页再输入
        elif cmdType.value == 4.1:
            #输入类型
            type = sheet1.row(i)[1].value
            #输入的值
            inputValue = inputConfig(type)
            t = 0
            while t < 20:
                pyautogui.keyDown('backspace')
                pyautogui.keyUp('backspace')
                t += 1
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)
        #5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet1.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        #6代表滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = sheet1.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动",int(scroll),"距离")
        #7代表判断时机
        elif cmdType.value == 7.0:
            #取图片名字 形式为: 1.png,2.png 或者 1.png
            img = "images/" + sheet1.row(i)[1].value
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            judge(img,reTry)
            print()
        i += 1