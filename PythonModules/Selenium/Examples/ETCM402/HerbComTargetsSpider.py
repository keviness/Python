import pandas as pd
from selenium import webdriver
import time as t
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#get直接返回，不再等待界面加载完成
#desired_capabilities = DesiredCapabilities.EDGE
#desired_capabilities["pageLoadStrategy"] = "none"
#cache path
path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/ETCM402/Compound&Target/402Com&Target/'
driver = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
url = 'http://www.tcmip.cn/ETCM/index.php/Home/Index/yc_details.html?id='

def getHerbNames(file):
    dataFrame = pd.read_excel(file)
    data = dataFrame.iloc[0:,:].values
    #print('data:\n', data)
    herbList = data[:, 0]
    #print('herbList:\n', herbList)
    return herbList

#模拟浏览器
def getHerbTargetsHtml(herbList):
    for i in range(258,len(herbList)+1):
        driver.get(url+str(i))
        numLabel = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[1]')
        numLabelText = numLabel.get_attribute('innerHTML')
        #print('numLabelHtml:\n', numLabelText)
        num = int(numLabelText.split(' ')[-2])
        if num > 10:
            buttonClick = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[2]/span/button')
            buttonClick.click()
            topBtnUi = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[2]/span/ul')
            topBtns = topBtnUi.find_elements_by_tag_name('li')
            #print('topBtns:\n',topBtns)
            topBtns[-1].click()
        table = driver.find_element_by_xpath('//*[@id="reportTable00"]')
        #tableHtml = table.get_attribute('outerHTML')
        #print('tableHtml:\n', tableHtml)
        tableHtml = table.get_attribute('outerHTML')
        dataFrame = pd.read_html(tableHtml)
        dataFrame[0].to_excel(path+f'{herbList[i-1]}.xlsx')
        print(f'write{i-1} {herbList[i-1]} to excel file successfully!')
    driver.close()
    
if __name__ == '__main__':
    file = path + '402中药信息.xlsx'
    herbList = getHerbNames(file)
    getHerbTargetsHtml(herbList)