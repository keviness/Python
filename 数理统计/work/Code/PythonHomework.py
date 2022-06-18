#---python homework---
# coding: utf-8
# env: python 3.8

inputPath = '/Users/kevin/Desktop/program files/python/数理统计/work/Data/十年内江西与广东两地进出口数据.txt'

#--数据读入及预处理--
def getData():
    with open(inputPath, 'r', encoding='utf-8') as file:
        textList = file.read().splitlines()
        file.close()
        #print('text:\n', textList)
    resultList = [eStr.split(',') for eStr in textList]
    #print('result:\n', resultList)
    return resultList

#--数据查询--
def queryList(myList, year, province):
    #print('resultList:\n', resultList)
    if year=='' or year == '\n'  : year = '0'
    if province == '' or province == '\n' : province = '0'
    if year!='0' and eval(year) not in range(2011,2021,1):print('查询年份输入错误，请重新输入！'); return
    if province!='0' and province not in ['广东省','江西省']:print('查询省份输入错误，请重新输入！'); return
    if year=='' and province=='':
        print('您没有输入正确的年份和省份，请重新输入！')
        return
    elif year!='0' and province=='0':
        Result = [arr for arr in myList if arr[0] == year]
        printResult(Result)
        return Result
    elif year=='0' and province!='0':
        Result = [arr for arr in myList if arr[1] == province]
        printResult(Result)
        return Result
    else:
        Result = [arr for arr in myList if arr[0] == year and arr[1] == province]
        printResult(Result)
        return Result

#--数据统计-- 
def dataAnalyse(myList):
    print('数据统计及分析'.center(40, '-'))
    jinChuKouSum = sum([eval(arr[2]) for arr in myList])
    print('\n十年内，两省进出口数据\n总和：', jinChuKouSum, '\n平均值：',jinChuKouSum/10)
    GDjinChuKouSum = sum([eval(arr[2]) for arr in myList if arr[1]=='广东省'])
    print('\n十年内，广东省进出口数据\n总和：', GDjinChuKouSum, '\n平均值：',GDjinChuKouSum/10)
    JXjinChuKouSum = sum([eval(arr[2]) for arr in myList if arr[1]=='江西省'])
    print('\n十年内，江西省进出口数据总和：', JXjinChuKouSum, '\n平均值：',JXjinChuKouSum/10)
    
    jinKouSum = sum([eval(arr[3]) for arr in myList])
    print('\n十年内，两省进口数据\n总和：', jinKouSum, '\n平均值：',jinKouSum/10)
    GDjinKouSum = sum([eval(arr[3]) for arr in myList if arr[1]=='广东省'])
    print('\n十年内，广东省进口数据\n总和：', GDjinKouSum, '\n平均值：',GDjinKouSum/10)
    JXjinKouSum = sum([eval(arr[3]) for arr in myList if arr[1]=='江西省'])
    print('\n十年内，江西省进口数据\n总和：', JXjinKouSum, '\n平均值：',JXjinKouSum/10)
    
    chuKouSum = sum([eval(arr[4]) for arr in myList])
    print('\n十年内，两省出口数据\n总和：', chuKouSum, '\n平均值：',chuKouSum/10)
    GDchuKouSum = sum([eval(arr[4]) for arr in myList if arr[1]=='广东省'])
    print('\n十年内，广东省出口数据\n总和：', GDchuKouSum, '\n平均值：',GDchuKouSum/10)
    JXchuKouSum = sum([eval(arr[4]) for arr in myList if arr[1]=='江西省'])
    print('\n十年内，江西省出口数据\n总和：', JXchuKouSum, '\n平均值：',JXchuKouSum/10)
    pass

#--显示结果--
def printResult(resultList):
    print('数据查询结果'.center(40, '-'))
    resultStr = []
    for elist in resultList:
        resultStr.append('\t'.join(elist))
    resultQueryStr = '\n'.join(resultStr).strip(' ')
    print(resultQueryStr)

#--增加数据--
def addData():
    print('数据添加'.center(40, '-'))
    text = input('请输入需要添加的数据（例如:2011,广东省,100679396.3,56321600,44357796.3）:\n')
    if text == '': print('请输入数据！');return
    with open(inputPath, 'a', encoding='utf-8') as file:
        file.write(text+'\n')
        file.close()
    print('数据添加成功！')
    
def mainMenu():
    myList = getData()
    while True:
        print('主菜单'.center(40, '-'))
        checkInput = input('请选择需要的功能\na. 数据查询\nb. 数据统计及分析\nc. 数据添加\nd. 退出\n')
        if checkInput == None: continue
        if checkInput == 'a':
            while True:
                print('数据查询'.center(40, '-'))
                print('数据查询提示：\n若仅按省份查询，请按回车跳过年份输入，只输入省份\n若仅按年份查询请按回车跳过省份输入，只输入年份\n')
                year = input('请输入查询的年份:\n')
                province = input('请输入查询的省份:\n')
                queryResult = queryList(myList, year, province)
                if queryResult == None: continue
                else: break
        elif checkInput == 'b': dataAnalyse(myList)
        elif checkInput == 'c': addData()
        elif checkInput == 'd': break
        else: print('功能选择错误，请重新选择！')
        
if __name__ == '__main__':
    mainMenu()