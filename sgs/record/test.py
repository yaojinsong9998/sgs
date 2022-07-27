import pyautogui
import time

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def mouseClick(clickTimes,lOrR,img,reTry,imgMap):
    print("正在寻找:" + img)
    if imgMap.__contains__(img) == True:
        conf = imgMap[img]
    else:
        conf = 0.8
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                print(location)
                print(location.x)
                print(location.y)
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到" + img +",0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
            i += 1
            time.sleep(0.1)

map = {}

