import time

import xlrd

from sgs.common.taskById import mainWork2
from sgs.utils.dataCheck import dataCheck
from sql.select import selectByDate
from sql.update import updateDay


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)


def renwu():
    file = 'xls/renwu.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)

    data = selectByDate(None, 0)
    num = str(len(data))
    print("共有" + num + "个天账号")

    i = 0
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(0))
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
            print("开始做任务第" + str((j + 1)) + "个号")
            res = mainWork2(int(i), sheet1, data[j], "images/renwu/")
            # 更新天数
            updateDay(id)
            print("已成功做任务账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')


if __name__ == '__main__':
    renwu()
