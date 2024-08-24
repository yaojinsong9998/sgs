import time

import xlrd

from sgs.common.taskById import mainWork2
from sgs.utils.dataCheck import dataCheck
from sql.select import selectByDate, selectYjs, selectFirstYjs, selectYjs2
from sql.update import updateDay, updateStatus


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)


def runOne():
    file = 'xls/richangshouji.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: 0.第一天（月卡版) 1.第二天（月卡版) 2.第三天（月卡版) 3.第四天(月卡版)'
                  '4.第五天(月卡版) 5.第六天(月卡版) 6.第七天(月卡版) 7.七天后（月卡版)')
    date = '2024-07-15'
    selectItem = int(index)
    if selectItem == 0:  # 第一天
        data = selectFirstYjs(date)
    if selectItem == 1:  # 第二天
        data = selectByDate(date, 1)
    if selectItem == 2:  # 第三天
        data = selectByDate(date, 2)
    if selectItem == 3:  # 第四天
        data = selectByDate(date, 3)
    if selectItem == 4:  # 第五天
        data = selectByDate(date, 4)
    if selectItem == 5:  # 第六天
        data = selectByDate(date, 5)
    if selectItem == 6:  # 第七天
        data = selectByDate(date, 6)
    if selectItem == 7:  # 第七天
        data = selectByDate(date, 7)
    num = len(data)
    print("共有" + str(num) + "天账号")

    i = 0
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备执行')

    # 数据检查
    checkCmd = dataCheck(sheet1)
    j = 0
    if checkCmd:
        while j < int(num):
            pre = time.time()
            id = data[j][0]
            print(f"当前总进度：{j}/{num}".format(j, num))
            print("开始日常第" + str((j + 1)) + "个号")
            res = mainWork2(int(i), sheet1, data[j], "images/richang/")
            if res == 'break':
                j += 1
                updateStatus(id)
                continue
            # 更新天数
            if selectItem != 0:
                updateDay(id)
            print("已成功完成账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')


def runBatch(date):
    file = 'xls/richang.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)

    selectItems = [8,7,6,5,4,3,2,1]
    # selectItems = [1, 2, 3, 4, 5, 6, 7, 8]
    num8to30 = len(selectYjs2(date, 7)) # 当前天 为第八到三十天的账号数量
    k = 0

    num2 = len(selectYjs(date, 1)) # 当前天 为第二天签到的账号数量
    num3 = len(selectYjs(date, 2)) # 当前天 为第三天签到的账号数量
    num4 = len(selectYjs(date, 3)) # 当前天 为第四天签到的账号数量
    num5 = len(selectYjs(date, 4)) # 当前天 为第五天签到的账号数量
    num6 = len(selectYjs(date, 5)) # 当前天 为第六天签到的账号数量
    num7 = len(selectYjs(date, 6))  # 当前天 为第七天签到的账号数量
    numgt30 = len(selectYjs(date, 30)) # 当前天 为大于等于三十天的账号数量

    sum = num2 + num3 + num4 + num5 + num6 + num7 + num8to30 + numgt30
    print(f"第二天账号数量 : {num2}")
    print(f"第三天账号数量 : {num3}")
    print(f"第四天账号数量 : {num4}")
    print(f"第五天账号数量 : {num5}")
    print(f"第六天账号数量 : {num6}")
    print(f"第七天账号数量 : {num7}")
    print(f"第八到三十天账号数量 : {num8to30}")
    print(f"第三十天及以后天账号数量 : {numgt30}")
    print("一共有" + str(sum) + "个天账号")

    sumSecondTime = num2 * 120  + num3 * 120 + num4 * 120 + num5 * 120 + num6 * 150 \
                    + num7 * 120 + num8to30 * 100 + numgt30 * 90
    hourTime = sumSecondTime // 3600
    minuteTime = (sumSecondTime % 3600) // 60

    print(f"预计总耗时{sumSecondTime}秒,合计{hourTime}小时{minuteTime}分钟")

    for selectItem in selectItems:
        if selectItem == 7:  # 七天后
            data = selectYjs2(date, 7)
        if selectItem == 1:  # 第二天
            data = selectYjs(date, 1)
        if selectItem == 2:  # 第三天
            data = selectYjs(date, 2)
        if selectItem == 3:  # 第四天
            data = selectYjs(date, 3)
        if selectItem == 4:  # 第五天
            data = selectYjs(date, 4)
        if selectItem == 5:  # 第六天
            data = selectYjs(date, 5)
        if selectItem == 6:  # 第七天
            data = selectYjs(date, 6)
        if selectItem == 8:  # 第三十天后
            data = selectYjs(date, 30) # 88s
        print(f"共有" + str(len(data)) + "个天账号")
        num = len(data)
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
                print(f"当前总进度：{k}/{sum}".format(k, sum))
                print(f"当前天进度：{j}/{num}".format(j, num))
                print("开始注册第" + str((j + 1)) + "个号")
                res = mainWork2(int(i), sheet1, data[j], "images/richang/")
                if res == 'break':
                    j += 1
                    updateStatus(id)
                    continue
                # 更新天数
                updateDay(id)
                print("已成功浇水账号: id为" + id)
                now = time.time()
                print("当前账号耗时:" + str(now - pre))
                j += 1
                k += 1
        else:
            print('表格没有此单元格')


if __name__ == '__main__':
    # runOne()

    date = '2024-08-24'
    runBatch(date)
