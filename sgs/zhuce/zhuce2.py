import xlrd
import time

from sgs.utils.dataCheck import dataCheck
from sgs.common.task import mainWork
from sgs.zhuce.zhuceUtils import map
from sql.select import selectLastId, selectDetailById, selectNumByDate, selectByDate
from sql.update import updateFinish, updateStatus, updateDay
from sgs.chongzhi.Utils.taskById import mainWork2

def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)

def updateNetWork():
    file = 'cmd2.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(0)
    i = 0
    print('准备切换网络')
    # 数据检查
    checkCmd = dataCheck(sheet1)
    if checkCmd:
        mainWork2(i, sheet1, 0)
    else:
        print('输入有误或者已经退出!')
    print('已成功切换网络')

def before():
    file = 'zhuce.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    index = 5
    i = 0
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    checkCmd = dataCheck(sheet1)
    j = 0
    if checkCmd:
        pre = time.time()
        res = mainWork2(int(i), sheet1, 0)
        now = time.time()
        print("当前账号耗时:" + str(now - pre))
        j += 1
    else:
        print('表格没有此单元格')

def runOne():
    file = 'zhuce.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    index = 6
    date = None
    selectItem = int(index)
    if selectItem == 6:
        data = selectByDate(date, 0)
    print("共有" + str(len(data)) + "个天账号")
    num = str(len(data))
    i = 0
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

if __name__ == '__main__':
    #文件名
    file = 'zhuce.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: 0.做一次 1.注册\n')
    date = getTodayDate()
    todayNum = selectNumByDate(date)
    print('今日已注册' + str(todayNum) + "个账号")
    num = input('要注册多少个\n')
    i = input('选择从第几行开始\n')
    #通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备进行三国杀账号注册')
    #数据检查f
    checkCmd = dataCheck(sheet1)
    begin = time.time()
    j = 0
    if checkCmd:
        while j < int(num):
            #满10个切网络
            if j != 0 and j % 10 == 0:
                print("等待切换网络...")
                updateNetWork()
                time.sleep(1)
            pre = time.time()
            print("开始注册第" + str((j + 1)) + "个号")
            mainWork(int(i), sheet1, map,j + 1,num)
            #获取刚注册的账号Id
            id = selectLastId()
            #更新完成标记
            updateFinish(id)
            # 输出该账号的信息
            info = selectDetailById(id)
            print("已成功注册账号\n")
            print(info)
            now = time.time()
            print("当前账号耗时:" + str(now - pre))
            j += 1;
    else:
        print('表格没有此单元格')
    end = time.time()
    print("本次总耗时:" + str(end - begin))

    before()
    runOne()

