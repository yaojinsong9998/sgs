import time

import xlrd

from sgs.common.taskById import mainWork2
from sgs.utils.dataCheck import dataCheck
from sql.select import selectUserByData, selectNumByDate
from sql.update import updateCost

def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)

def chongzhi():
    file ='xls/chongzhi.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    index = 0
    date = getTodayDate()

    num = selectNumByDate(date)
    #获取账号信息
    data = selectUserByData(date,num)
    i = 0
    #通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备进行三国杀账号充值')
    #数据检查
    checkCmd = dataCheck(sheet1)
    j = 0
    if checkCmd:
        while j < int(num):
            pre = time.time()
            id = data[j][0]
            print("开始充值第" + str((j + 1)) + "个号: id为" + id)
            mainWork2(int(i), sheet1, data[j],"images/chongzhi/")
            #更新完成标记
            updateCost(id)
            print("已成功充值账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')

if __name__ == '__main__':
    chongzhi()