from selenium import webdriver
import pandas as pd
import pickle, json
import os
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/Data/ChainLink.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/result/'
cookiePath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/result/DrugBankCookies.pickle'
# ---绕过人机识别---
options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
options.add_argument("--lang=zh-CN")
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', options=options)
jsText = open('/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/Code/stealth.min.js', 'r').read()
bor.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    # 这里的操作大概就是把控制台中的window.navigator.webdriver =undefined  赋值   因为人机操作会认为是Ture
        "source": '''Object.defineProperties(navigator,webdriver:{get:()=> undefined}'''
    })
bor.maximize_window()

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath, sheet_name='scrawlData')
    data = dataFrame.loc[:, ['TargetName','ChainLink']].values
    #print('data:\n', data)
    TargetNameList = data[:,0]
    ChainLinkList = data[:,1]
    #print('herbList:\n', TargetNameList)
    return TargetNameList, ChainLinkList
 
def CrawlHerbInfo(TargetNameList, ChainLinkList):
    #bor.get(ChainLinkList[0])
    bor.execute_script('window.location="'+ChainLinkList[0]+'"')
    uniportIDList = []
    for TargetName, ChainLink in zip(TargetNameList, ChainLinkList):
        #loadCookies(cookiePath, bor)
        #print(f'{herbID}:{herbName}')
        #bor.get(ChainLink)
        bor.execute_script('window.location="'+ChainLink+'"')
        #x = input("随便输点啥")
        #writeCookies(bor)
        #if not bor.find_element_by_xpath('/html/body/main/div/div[2]/dl[1]/dd[4]/table/tbody/tr/td[2]/a'):
        #    continue
        uniportIDHtml = bor.find_element_by_xpath('/html/body/main/div/div[2]/dl[1]/dd[4]/table/tbody/tr/td[2]/a')
        uniportID = uniportIDHtml.get_attribute('innerHTML')
        uniportIDList.append(uniportID)
        print(f'{TargetName}:{uniportID}: {ChainLink}')
    dataFrame = pd.DataFrame({
                               'TargetName':TargetNameList,
                               'ChainLink':ChainLinkList,
                               'uniportID':uniportIDList
                            }) 
    dataFrame.to_excel(outputPath+'targetUniport.xlsx', index=False)
    print('write to excel file successfully!')
    bor.close()
    
def writeCookies(bor):
    dictCookies = bor.get_cookies()  # 获取list的cookies
    #print('dictCookies:\n', dictCookies)
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open(outputPath+'DrugBankCookies.pickle', 'w') as f:
        f.write(jsonCookies)
        f.close()
    print('cookies保存成功！')

def loadCookies(cookiesPath, bor):
    with open(cookiesPath, 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        cookie_dict = {
            'domain': 'go.drugbank.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'path': '/',
            'secure': cookie.get('secure')
        }
        bor.add_cookie(cookie_dict)
    return bor
        
if __name__ == '__main__':
    TargetNameList, ChainLinkList = getContents(inputPath)
    CrawlHerbInfo(TargetNameList, ChainLinkList)
    