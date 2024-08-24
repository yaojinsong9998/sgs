import time

import xlrd

from sgs.common.taskById import mainWork2
from sgs.utils.dataCheck import dataCheck
from sql.select import selectHuoDong
from sql.update import updateHuoDong


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)



def runBatch():
    file = 'xls/richang3.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    k = 0

    data = selectHuoDong()
    sum = len(selectHuoDong())
    print("一共有" + str(sum) + "个账号")

    sumSecondTime = sum * 140
    hourTime = sumSecondTime // 3600
    minuteTime = (sumSecondTime % 3600) // 60

    print(f"预计总耗时{sumSecondTime}秒,合计{hourTime}小时{minuteTime}分钟")

    num = len(data)
    i = 1
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(0)
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
            res = mainWork2(int(i), sheet1, data[j], "images/huodong/")
            updateHuoDong(id)
            print("已成功浇水账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
            k += 1
    else:
        print('表格没有此单元格')


if __name__ == '__main__':
    runBatch()