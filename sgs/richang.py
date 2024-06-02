import time

import xlrd

from sgs.chongzhi.Utils.taskById import mainWork2
from sgs.common.dataCheck import dataCheck
from sql.select import selectByDate, checkZhanghao, selectYjs, selectFirstYjs
from sql.update import updateDay, updateStatus


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)

def runOne():
    file = 'cmd2.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: 0.做一次 1.注册 2.第一天 3.第二天 4.第三天 5.第四天 6.校验 7.七天后'
                  '8.第一天（月卡版) 9.第二天（月卡版) 10.第三天（月卡版) 11.第四天(月卡版)'
                  '12.第五天(月卡版)13.第六天(月卡版) 14.第七天(月卡版)')
    # date = '2024-03-10'
    date = None
    selectItem = int(index)
    if selectItem == 2:
        data = selectByDate(date, 0)
    if selectItem == 3:
        data = selectByDate(date, 1)
    if selectItem == 4:
        data = selectByDate(date, 2)
    if selectItem == 5:
        data = selectByDate(date, 3)
    if selectItem == 6:
        data = checkZhanghao(date)
    if selectItem == 7:
        date = '2024-04-15'
        data = selectYjs(date, 7)
    if selectItem == 8:
        date = '2024-06-01'
        data = selectFirstYjs(date, 1)
    if selectItem == 9:
        date = '2024-04-13'
        data = selectYjs(date, 1)
    if selectItem == 10:
        date = '2024-04-13'
        data = selectYjs(date, 2)
    if selectItem == 11:
        date = '2024-04-13'
        data = selectYjs(date, 3)
    if selectItem == 12:
        date = '2024-04-13'
        data = selectYjs(date, 4)
    if selectItem == 13:
        date = '2024-04-13'
        data = selectYjs(date, 5)
    if selectItem == 14:
        date = '2024-04-13'
        data = selectYjs(date, 5)
    print("共有" + str(len(data)) + "个天账号")
    num = input('要浇水多少个:-1代表全部浇水 -2代表退出\n')
    if num == '-1':
        num = str(len(data))
    elif num == '-2':
        exit()
    i = input('选择从第几行开始\n')
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备执行')
    # 定时执行
    # time.sleep(4200)
    # 数据检查
    checkCmd = dataCheck(sheet1)
    j = 0
    if checkCmd:
        while j < int(num):
            pre = time.time()
            id = data[j][0]
            print("开始注册第" + str((j + 1)) + "个号")
            res = mainWork2(int(i), sheet1, data[j])
            if res == 'break':
                j += 1
                updateStatus(id)
                continue
            # 更新天数
            if selectItem != 8:
                updateDay(id)
            print("已成功浇水账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')

def runBatch(date):
    file = 'cmd2.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # selectItems = [7,9, 10, 11, 12, 13,14]
    # selectItems = [7, 9,10,11, 12, 13,14]
    selectItems = [7, 14, 13, 12, 11, 10, 9]
    for selectItem in selectItems:
        if selectItem == 7:
            data = selectYjs(date, 7)
        # if selectItem == 8:
        #     data = selectFirstYjs(date, 1)
        if selectItem == 9:
            data = selectYjs(date, 1)
        if selectItem == 10:
            data = selectYjs(date, 2)
        if selectItem == 11:
            data = selectYjs(date, 3)
        if selectItem == 12:
            data = selectYjs(date, 4)
        if selectItem == 13:
            data = selectYjs(date, 5)
        if selectItem == 14:
            data = selectYjs(date, 6)
        print("共有" + str(len(data)) + "个天账号")
        num = str(len(data))
        i = 1
        # 通过索引获取表格sheet页
        sheet1 = wb.sheet_by_index(selectItem)
        print('准备执行')
        # 数据检查
        checkCmd = dataCheck(sheet1)
        j = 0
        if checkCmd:
            while j < int(num):
                pre = time.time()
                id = data[j][0]
                print("开始注册第" + str((j + 1)) + "个号")
                res = mainWork2(int(i), sheet1, data[j])
                if res == 'break':
                    j += 1
                    updateStatus(id)
                    continue
                # 更新天数
                if selectItem != 8:
                    updateDay(id)
                print("已成功浇水账号: id为" + id)
                now = time.time()
                print("当前账号耗时:" + str(now - pre))
                j += 1
        else:
            print('表格没有此单元格')

if __name__ == '__main__':
    # runOne()
    time.sleep(2400)
    date = '2024-06-02'
    runBatch(date)
