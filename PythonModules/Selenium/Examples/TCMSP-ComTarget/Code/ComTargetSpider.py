from selenium import webdriver
import pandas as pd
import time
#from selenium.webdriver.support.select import Select

# 设置参数
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Data/502Herbs.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Result/'

def getHerbNames(file):
    dataFrame = pd.read_excel(file)
    data = dataFrame.iloc[0:,:].values
    #print('data:\n', data)
    herbList = data[:, 0]
    #print('herbList:\n', herbList)
    return herbList

def CrawlHerbInfo(herbName, bor):
    # 向搜索框中录入关键词
    search_label = bor.find_element_by_xpath('//*[@id="inputVarTcm"]')
    search_label.send_keys(herbName)
    search_input = bor.find_element_by_xpath('//*[@id="searchBtTcm"]')
    search_input.click()
    click_herb = bor.find_element_by_xpath('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[3]/a')
    click_herb.click()
    #bor.find_element_by_xpath('/html/body').click()
    click_target = bor.find_element_by_xpath('//*[@id="tabstrip"]/ul/li[2]/a')
    #print('click_target:\n', click_target)
    #bor.execute_script("arguments[0].click", click_target)
    click_target.click()
    
    dataFrame = pd.DataFrame()
    i = 0
    while True:
        table = bor.find_element_by_xpath('//*[@id="grid2"]/div[2]')
        #table_text = table.get_attribute('innerText')
        #if table_text == '': continue
        table_html = table.get_attribute('innerHTML')
        #print('table_html:\n', table_text)
        data = pd.read_html(table_html)
        dataFrame = dataFrame.append(data, ignore_index=True)
        #print('dataFrame:\n', dataFrame)
        next_page = bor.find_element_by_xpath('//*[@id="grid2"]/div[3]/a[3]')
        #print('next_page:\n', next_page)
        next_page_class = next_page.get_attribute('class')
        #print('next_page_class:\n', next_page_class)
        if i==0: time.sleep(2.5); i += 1
        if next_page_class == 'k-link k-state-disabled':
            break
        else:
            next_page.click()
    dataFrame.columns = ['MOLID','MoleculeName','target','Source','status']
    dataFrame.to_excel(outputPath+herbName+'.xlsx')
    print(f'write {herbName} information to excel successfully!')

def main(file):
    herbList = getHerbNames(file)
    bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver')
# 对指定的url发起请求
    bor.get('https://old.tcmsp-e.com/tcmspsearch.php?qr=Panax%20Ginseng%20C.%20A.%20Mey.&qsr=herb_en_name&token=17a7c038009e05b85ee72af43ac7a6d1')
    input_enter = bor.find_element_by_xpath('//*[@id="details-button"]')
    input_enter.click()
    enter_input = bor.find_element_by_xpath('//*[@id="proceed-link"]')
    enter_input.click()

    for herb in herbList:
        CrawlHerbInfo(herb, bor)

if __name__ == '__main__':
    file = inputPath
    main(file)