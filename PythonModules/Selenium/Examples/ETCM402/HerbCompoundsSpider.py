import pandas as pd
from selenium import webdriver
import time as t
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#get直接返回，不再等待界面加载完成
#desired_capabilities = DesiredCapabilities.EDGE
#desired_capabilities["pageLoadStrategy"] = "none"
#cache path
#driver.maximize_window()
#driver.implicitly_wait(10)

num1 = 7443
#num = 1000
path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/ETCM402/Compound&Target/'

driver = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
url = 'http://www.tcmip.cn/ETCM/index.php/Home/Index/cf_details.html?id='
#模拟浏览器
def getHerbTargetsHtml(url, start, end):
    resultDataFrame = pd.DataFrame()
    for i in range(start, end+1):
        driver.get(url+str(i))
        table = driver.find_element_by_xpath('//*[@id="table"]')
        tableHtml = table.get_attribute('outerHTML')
        tableDataFrame = pd.read_html(tableHtml)[0]
        colums = tableDataFrame['Unnamed: 0'].values
        del tableDataFrame['Unnamed: 0']
        #print('tableDataFrame:\n', tableDataFrame)
        #tableDataFrame = tableDataFrame.T
        #dataFrame = pd.DataFrame()
        #dataFrame = dataFrame.append(tableDataFrame, ignore_index=True)
        resultDataFrame = resultDataFrame.append(tableDataFrame.T, ignore_index=True)   
        #print('dataFrame:\n', resultDataFrame)
    resultDataFrame.columns = colums
    resultDataFrame.to_excel(path+str(start)+'_'+str(end)+'compounds.xlsx', index=True)
    print('write To excel file successfully!')
    return resultDataFrame

    
if __name__ == '__main__':
    #file = path + '402中药信息.xlsx'
    #herbList = getHerbNames(file)
    startEndList = [(1002,3001), (3001,4001), (4001,5001),(5001,6001),(6001,7001),(7001,7443)]
    dataFrameResult = pd.DataFrame()
    for start, end in startEndList:
        dataFrame = getHerbTargetsHtml(url, start, end)
        dataFrameResult = dataFrameResult.append(dataFrame, ignore_index=True)
    dataFrameResult.to_excel(path+'compoundsResult.xlsx')
    driver.close()