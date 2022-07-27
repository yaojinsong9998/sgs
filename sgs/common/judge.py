import pyautogui
import time

#保证reTry > 1
def judge(img,reTry):
    print("正在判断是否合法!")
    images = img.split(',')
    #点reTry次
    if reTry > 1:
        i = 1
        while i < reTry + 1:
            if len(images) == 1:
                location = pyautogui.locateCenterOnScreen(images[0], confidence=0.8)
                if location is not None:
                    return False
            elif len(images) == 2:
                location1 = pyautogui.locateCenterOnScreen(images[0], confidence=0.8)
                location2 = pyautogui.locateCenterOnScreen(images[1], confidence=0.8)
                if location1 is not None:
                    return False
                if location2 is not None:
                    return False
            i += 1
            time.sleep(0.1)
        return True

def judgeList(img,reTry):
    res = judge(img,reTry)
    if res == False:
        images = img.split(',')