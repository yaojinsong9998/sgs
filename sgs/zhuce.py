import xlrd
import time

from sgs.chongzhi.Utils.taskById import mainWork2
from sgs.common.dataCheck import dataCheck
from sgs.common.task import mainWork
from sgs.renwu import renwu
from sql.select import selectLastId, selectDetailById, selectNumByDate
from sql.update import updateFinish


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)

def before():
    file = 'xls/zhuce.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)

    index = 1

    row = 1  # 默认从第一行开始执行
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    checkCmd = dataCheck(sheet1)
    j = 0

    if checkCmd:
        pre = time.time()
        res = mainWork2(int(row), sheet1, None, "images/zhuce/")
        now = time.time()
        print("当前账号耗时:" + str(now - pre))
        j += 1
    else:
        print('表格没有此单元格')

def zhuce():
    # 文件名
    file = 'xls/zhuce.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)

    index = 0

    date = getTodayDate()
    todayNum = selectNumByDate(date)
    print('今日已注册' + str(todayNum) + "个账号")

    num = input('准备注册多少个\n')

    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(int(index))
    print('准备进行三国杀账号注册')

    row = 1  # 默认从第一行开始执行
    # 数据检查f
    checkCmd = dataCheck(sheet1)
    begin = time.time()
    j = 0
    map = {}
    if checkCmd:
        while j < int(num):
            pre = time.time()
            print("开始注册第" + str((j + 1)) + "个号")
            mainWork(int(row), sheet1, map, j + 1, num, "images/zhuce/")
            # 获取刚注册的账号Id
            id = selectLastId()
            # 更新完成标记
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


if __name__ == '__main__':
    selectItem = input('选择任务类型: 0.注册(不做任务) 1.注册(做任务)\n')
    if selectItem == '0':
        zhuce()
    if selectItem == '1':
        zhuce()
        before()
        renwu()


