import pandas as pd
from selenium import webdriver
import time as t
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#get直接返回，不再等待界面加载完成
#desired_capabilities = DesiredCapabilities.EDGE
#desired_capabilities["pageLoadStrategy"] = "none"
#cache path
path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/HerbTargets/Compound&Target/'

def getHerbNames(file):
    dataFrame = pd.read_excel(file)
    data = dataFrame.iloc[0:,:].values
    #print('data:\n', data)
    herbList = data[:, 0]
    #print('herbList:\n', herbList)
    return herbList

#模拟浏览器
def getHerbTargetsHtml(herbList):
    driver = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
    url = 'http://www.tcmip.cn/ETCM/index.php/Home/Index/yc_details.html?id=1'
    #driver.maximize_window()
    #driver.implicitly_wait(10)
    driver.get(url)
    table = driver.find_element_by_xpath('//*[@id="reportTable00"]')
    tableHtml = table.get_attribute('outerHTML')
    #print('tableHtml:\n', tableHtml)
    #dataFrame = pd.DataFrame()
    
    label = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[1]')
    labelStrList = label.get_attribute('innerHTML').split(' ')
    nums = int(labelStrList[-2])
    dataFrame = pd.DataFrame()
    for e in range(0, (nums//20)):
            table = driver.find_element_by_xpath('//*[@id="reportTable00"]')
            tableHtml = table.get_attribute('outerHTML')
            data = pd.read_html(tableHtml)
            dataFrame = dataFrame.append(data, ignore_index=True)
            next_page = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[2]/ul/li[9]/a')
            next_url = next_page.get_attribute('href')
            driver.get(next_url)
    dataFrame.set_index('Chemical Component', inplace=True)
    #print('data:\n',dataFrame)
    dataFrame.to_excel(path+f'{herbList[0]}.xlsx')
    print(f'write {herbList[0]} to excel successfully!')
    
    for i in range(2, len(herbList)+1):
        # 跳转到新页面
        url = 'http://www.tcmip.cn/ETCM/index.php/Home/Index/yc_details.html?id={}'.format(i)
        js_new_window = 'window.location=\"'+url+'\"'
        # 执行js
        driver.execute_script(js_new_window)
        
        label = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[1]')
        labelStrList = label.get_attribute('innerHTML').split(' ')
        nums = int(labelStrList[-2])
        
        dataFrame = pd.DataFrame()
        for e in range(0, (nums//20)+1):
            if nums < 20:
                break
            table = driver.find_element_by_xpath('//*[@id="reportTable00"]')
            tableHtml = table.get_attribute('outerHTML')
            data = pd.read_html(tableHtml)
            dataFrame = dataFrame.append(data, ignore_index=True)
            next_page = driver.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[2]/ul/li[9]/a')
            next_url = next_page.get_attribute('href')
            driver.get(next_url)        
        #dataFrame.set_index('Chemical Component', inplace=True)
        dataFrame.to_excel(path+'{}.xlsx'.format(herbList[i-1]))
        print('write {} to excel successfully!'.format(herbList[i-1]))
    driver.close()
    
if __name__ == '__main__':
    file = path + '402中药信息.xlsx'
    herbList = getHerbNames(file)
    getHerbTargetsHtml(herbList)