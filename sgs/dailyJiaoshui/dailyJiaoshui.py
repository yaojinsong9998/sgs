import xlrd
import time

from sgs.chongzhi.Utils.taskById import mainWork
from sgs.common.dataCheck import dataCheck

from sql.select import selectNumByDate, selectDailyNum
from sql.update import updateCost, updateDay

if __name__ == '__main__':
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: 0.做一次 1.注册 2. 3.充值 4.第2-7天 5.日常\n')
    date = input('输入未更新账号的时间\n')
    #获取已经完成7日任务的且今天没有更新的账号（即没有浇水的账号）
    data = selectDailyNum(date)
    print("今天共有" + str(len(data)) + "个账号未浇水!")
    num = input('要浇水多少个:-1代表全部浇水 -2代表退出\n')
    if num == '-1':
        num = str(len(data))
    elif num == '-2':
        exit()
    i = input('选择从第几行开始\n')
    #通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备进行日常浇水')
    #数据检查
    checkCmd = dataCheck(sheet1)
    j = 0
    if checkCmd:
        while j < int(num):
            pre = time.time()
            id = data[j][0]
            print("开始浇水第" + str((j + 1)) + "个号: id为" + id)
            mainWork(int(i), sheet1,data[j])
            #更新天数
            updateDay(id)
            print("已成功浇水账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')
