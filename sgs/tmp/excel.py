import xlrd

from sql.shenfenzheng.insert import insertCard

def tmpExcel():
    file = 'shenfenzheng.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    index = input('选择单元格索引: \n')
    # 通过索引获取表格sheet页
    sheet = wb.sheet_by_index(int(index))
    i = 0
    while i < sheet.nrows:
        #获取行类型
        cmdType = sheet.row(i)[0]
        #获取行的值
        str = cmdType.value
        res = str.split('----')
        insertCard(res[1],res[0])
        i += 1

tmpExcel()