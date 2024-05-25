import xlrd
import time

from sgs.chongzhi.Utils.taskById import mainWork2
from sgs.common.dataCheck import dataCheck

from sql.select import selectUserByData, selectNumByDate
from sql.update import updateCost, updateDay

if __name__ == '__main__':
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: 0.做一次 1.注册 2. 3.充值 4.第2-7天 5.日常\n')
    date = '2024-04-20'
    num = input('要充值多少个:-1代表创建时间内的账号全部充值\n')
    if num == "-1":
        num = selectNumByDate(date)
    #获取账号信息
    data = selectUserByData(date,num)
    i = input('选择从第几行开始\n')
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
            mainWork2(int(i), sheet1, data[j])
            #更新完成标记
            updateCost(id)
            # #更新天数
            # updateDay(id)
            print("已成功充值账号: id为" + id)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1
    else:
        print('表格没有此单元格')
