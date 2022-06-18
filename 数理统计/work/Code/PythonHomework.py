#---python homework---
#encode: utf-8
#env: python 3.8

inputPath = '/Users/kevin/Desktop/program files/python/数理统计/work/Data/十年内江西与广东两地进出口数据.txt'

#--数据读入及预处理--
def getData():
    with open(inputPath, 'r') as file:
        textList = file.read().splitlines()
        file.close()
        print('text:\n', textList)
    resultList = [eStr.split(',') for eStr in textList]
    print('result:\n', resultList)
    return resultList

#--数据查询--
def queryList(myList, year, province):
    #print('resultList:\n', resultList)
    if year == '' or year == '\n' : year = '0'
    if province == '' or province == '\n' : year = '0'
    if eval(year) not in range(2011,2021,1):print('查询年份输入错误，请重新输入！'); return
    if province not in ['广东省','江西省']:print('查询省份输入错误，请重新输入！'); return
    if year=='' and province=='':
        print('您没有输入正确的年份和省份，请重新输入！')
        return
    elif year!='' and province=='':
        Result = [arr for arr in myList if arr[0] == year]
        print('查询结果：\n', Result)
        return Result
    elif year=='' and province!='':
        Result = [arr for arr in myList if arr[1] == province]
        print('查询结果：\n', Result)
        return Result
    else:Result = [arr for arr in myList if arr[0] == year and arr[1] == province]
    if len(Result) == 0:
        print('查询结果为空！\n')
    print('查询结果：\n', Result)
    return Result

def mainMenu():
    myList = getData()
    while True:
        print('主菜单'.center(38, '-'))
        checkInput = input('请选择需要的功能\na. 数据查询\nb. 数据统计及分析\nc. 退出\n')
        if checkInput == None: continue
        if checkInput == 'a':
            while True:
                year = input('请输入查询的年份（若不按年份查询请按回车）:\n')
                province = input('请输入查询的省份（若不按省份查询请按回车）:\n')
                queryResult = queryList(myList, year, province)
                if queryResult == None: continue
                else: break
        elif checkInput == 'b':
            break
        elif checkInput == 'c': break
if __name__ == '__main__':
    mainMenu()