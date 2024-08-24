import xlrd
import time

from sgs.common.taskById import mainWork2
from sgs.utils.dataCheck import dataCheck
from sgs.common.task import mainWork
from sql.select import selectLastId, selectDetailById, selectNumByDate, selectByDate
from sql.update import updateFinish, updateDay, updateFinishByPhone


def getTodayDate():
    times = time.time()
    local_time = time.localtime(times)
    return time.strftime("%Y-%m-%d", local_time)

def zhuce():
    # 文件名
    file = 'xls/zhuceshouji.xls'
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
            mainWork(int(row), sheet1, map, j + 1, num, "images/zhuceshouji/")
            # 获取刚注册的账号Id
            id = selectLastId()
            # 更新完成标记
            updateFinishByPhone(id)
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
    zhuce()


