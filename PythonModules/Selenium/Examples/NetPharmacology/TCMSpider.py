from selenium import webdriver
import pandas as pd
#from selenium.webdriver.support.select import Select

path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/data/'

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

    dataFrame = pd.DataFrame()
    while True:
        table = bor.find_element_by_xpath('//*[@id="grid"]/div[2]')
        table_html = table.get_attribute('innerHTML')
        #print('table_html:\n', table_html)
        data = pd.read_html(table_html)
        dataFrame = dataFrame.append(data, ignore_index=True)
        #print('dataFrame:\n', dataFrame)
        next_page = bor.find_element_by_xpath('//*[@id="grid"]/div[3]/a[3]')
        next_page_class = next_page.get_attribute('class')
        #print('next_page_class:\n', next_page_class)
        if next_page_class == 'k-link k-state-disabled':
            break
        else:
            next_page.click()
    dataFrame.to_excel(path+herbName+'.xlsx')
    print(f'write {herbName} information to excel successfully!')

def main(file):
    herbList = getHerbNames(file)
    bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
# 对指定的url发起请求
    bor.get('https://old.tcmsp-e.com/tcmspsearch.php?qr=Panax%20Ginseng%20C.%20A.%20Mey.&qsr=herb_en_name&token=17a7c038009e05b85ee72af43ac7a6d1')
    input_enter = bor.find_element_by_xpath('//*[@id="details-button"]')
    input_enter.click()
    enter_input = bor.find_element_by_xpath('//*[@id="proceed-link"]')
    enter_input.click()

    for herb in herbList:
        CrawlHerbInfo(herb, bor)

if __name__ == '__main__':
    file = path + 'Herbs.xlsx'
    main(file)
    
