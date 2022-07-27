import pyautogui
import time

#定义鼠标事件

def mouseClick(clickTimes,lOrR,img,reTry):
    print("正在寻找:" + img)
    conf = 0.8
    #点一次 在reTry绝对值秒内找不到则结束  TODO昵称可能会重复 通过改4次名字降低重复率
    if reTry <= -2:
        time.sleep(abs(reTry))
        location = pyautogui.locateCenterOnScreen(img, confidence=conf)
        if location is not None:
             pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
        else:
            print("在" + str(abs(reTry)) + "秒内未找到")
        time.sleep(0.1)
    #点一次 直到找到为止
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            #print("未找到" + img +",0.1秒后重试")
            time.sleep(0.1)
    #重复点
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    #点reTry次
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=conf)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
            i += 1
            time.sleep(0.5)