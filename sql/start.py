# 增加路径参数
# 增加code msg result
# 替换return
# 接口格式分为两种类型：
# public String queryTrendData() throws Exception {
# public String queryBuDimInfo() {

import os
import sys


# 判断是否为源码文件
def isCodeFile(filePath):
    if filePath.endswith(".java"):
        return True
    else:
        return False


# return map
def findResult(map2):
    print("当前函数生成的result:")
    result = "result.add(\"" + "code" + "\"," + "code" + ")" + ";" + "\n" + "result.add(\"" + "msg" + "\"," + "msg" + ")" + ";" + "\n"
    for item in map2:
        result = result + "result.add(\"" + item + "\"," + item + ")" + ";" + "\n"
    result = result + "return result;" + '\n'
    return result

#找到函数的结尾 并生成路径参数和result
def findFunctionEnd(i, lines, map1, map2):
    res = []
    while i < len(lines):
        line = lines[i]
        if line == ("    }" + '\n'):  # 函数的结尾
            print("当前函数生成的路径参数:")
            paramcontent = ""
            for item in map1:
                if map1[item] > 0:
                    # print(str(item) + "  " + str(map1[item]))
                    map1[item] = 0
                    paramcontent = paramcontent + ("@RequestParam(value = \"" + item + "\", required = false)")
                    paramcontent = paramcontent + " " + map2[item] + " " + item + "," + '\n' + '\t\t'
            paramcontent = paramcontent[0:-4]  # 去掉最后一个 ,
            print(paramcontent)
            # print("当前函数生成的result:")
            # result = "result.add(\"" + "code" + "\"," + "code" + ")" + ";" + "\n" + "result.add(\"" + "msg" + "\"," + "msg" + ")" + ";" + "\n"
            # for item in map2:
            #     result = result + "result.add(\"" + item + "\"," + item + ")" + ";" + "\n"
            # result = result + "return result;"
            # print(result)
            res.append(i)
            res.append(paramcontent)
            # res.append(result)
            break
        else:
            # 对于当前行中出现的map1中的元素 进行记录
            for item in map1:
                if item in line:  # 可能出现的问题是部分匹配
                    map1[item] = map1[item] + 1
            i = i + 1

    return res


# 判断当前函数是否应该更改 用来区别接口和非接口
def isNeedFunction(i, lines):
    while i < len(lines):
        line = lines[i]
        if "return SUCCESS;" in line:
            return True
        elif line == ("    }" + '\n'):
            break
        else:
            i = i + 1

    return False


# 生成文件内容
def produceFileContent(filePath, map1, map2):
    print("🔧正在生成文件内容--> " + filePath)
    num = 0
    with open(filePath, mode="r", encoding="utf-8") as oldFile, open("%s.bak" % filePath, mode="w",
                                                                     encoding="utf-8") as newFile:
        lines = [line for line in oldFile]  # 获取每行文本并增加到列表
        while num < len(lines):
            line = lines[num]
            line = line.strip()  # 去掉首位空格
            liebiao = line.split()  # 根据空格分割
            if "public" in liebiao and "String" in liebiao and "()" in liebiao[2] and "{" in liebiao:  # 对函数增加参数
                print("当前行数：" + str(num) + "函数名:" + liebiao[2])
                print("判断" + liebiao[2] + "函数是否需要增加参数...")
                if isNeedFunction(num + 1, lines) == True:
                    # 增加@GetMapping("/queryBusinessEffectOverViewByShopId")
                    mappingline = "@GetMapping(" + "\"/" + liebiao[2][0:-2] + "\"" + ")\n"
                    newFile.write(mappingline)
                    print("正在" + liebiao[2] + "函数体中搜索参数----")
                    res = findFunctionEnd(num + 1, lines, map1, map2)  # num + 1避免函数名中有参数
                    paramcontent = res[1]
                    liebiao[1] = "Object"  # 改返回类型
                    liebiao[2] = liebiao[2][0:-1] + paramcontent + ")"
                    line = '\t' + " ".join(liebiao) + '\n'
                    # 增加路径参数
                    newFile.write(line)
                    # 加局部变量
                    line = "Map < String, Object > result = new HashMap <> ();\nMap < String, Object > msg = new HashMap < String, Object > ();\nint code;\n"
                    newFile.write(line)
                else:
                    print(liebiao[2] + "函数不需要增加参数!")
            elif "return SUCCESS;" in lines[num] or "return ERROR;" in lines[num]:
                # length = len(lines[num]) - len("return SUCCESS;")
                # result = ""
                # for i in range(0,length):
                #     result = result + "\t"
                result = findResult(map2) + '\n'
                newFile.write(result)
            else:
                newFile.write(lines[num])
            num += 1
    os.remove(filePath)
    os.rename("%s.bak" % filePath, filePath)
    print("✅文件内容生成完成！--> " + filePath)
    print("---------------------------------------")
    return True


# 获取成员变量
# 例:
# map1 = {'a1':0,'a2':0,'a3':0,'a4':0}  用于判断函数中是否出现该成员变量
# map2 = {'a1':'int','a2':'int','a3':'int','a4':'int'} 用于记录成员变量类型
# map = [map1,map2]
# filter 可能出现的变量类型 用于排除service的影响
def getMap(filePath):
    map = []
    map1 = {}
    map2 = {}
    filter = ['Integer', 'String', 'int','List<String>']
    if isCodeFile(filePath) == False:
        print("⚠️ 此文件不是源码文件，忽略处理 ... --> " + filePath)
        return
    print("🔧正在获取成员变量信息--> " + filePath)
    with open(filePath, mode="r", encoding="utf-8") as oldFile:
        for line in oldFile:
            line = line.strip()  # 去掉首位空格
            liebiao = line.split()  # 根据空格分割
            if "private" in liebiao and "{" not in liebiao:  # 成员变量判断条件
                log = ""  # 日志信息
                type = liebiao[1]
                param = liebiao[2].strip(';')
                log = log + "变量类型:" + type + "变量名:" + param
                print(log)
                if type in filter:  # 主要用于排除service的影响
                    map1[param] = 0
                    map2[param] = type
    print("✅成员变量信息获取完成!--> " + filePath)
    map.append(map1)
    map.append(map2)
    if len(map[0]) > 0:
        print("当前成员变量信息:")
        print(map1)
        print(map2)
    else:
        print(filePath + "不包含成员变量")
        print("---------------------------------------")
    return map


# 遍历路径，获得所有文件
def foreachPath(currentPath):
    num1 = 0  # 文件总数
    num2 = 0  # java文件个数
    for root, dirs, files in os.walk(currentPath, topdown=False):
        for file in files:
            filePath = os.path.join(root, file)
            num1 += 1
            map = getMap(filePath)
            if isCodeFile(filePath) == True:
                num2 += 1
            if map != None and len(map[0]) > 0:
                produceFileContent(filePath, map[0], map[1])
    return [num1, num2]


# 入口
def main():
    currentPath = input("\n请输入需要处理的文件目录：\n")
    print("需要处理的文件目录为:" + currentPath)
    filenum = foreachPath(currentPath)
    print("共有" + str(filenum[0]) + "个文件!")
    print("已处理" + str(filenum[1]) + "个java文件!")


main()
