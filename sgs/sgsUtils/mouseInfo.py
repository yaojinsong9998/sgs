import pyautogui

#用于找到屏幕当前鼠标位置
while True:
    info = pyautogui.mouseInfo()
    print(info)
