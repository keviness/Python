from selenium import webdriver
import pandas as pd
#from selenium.webdriver.support.select import Select

path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/data/'
bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
# 对指定的url发起请求
bor.get('https://old.tcmsp-e.com/browse.php?qc=herbs')

# 进行标签定位
input_enter = bor.find_element_by_xpath('//*[@id="details-button"]')
input_enter.click()
enter_input = bor.find_element_by_xpath('//*[@id="proceed-link"]')
enter_input.click()
#print('text:\n', bor.page_source)

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

dataFrame.to_excel(path+'Herbs.xlsx')
print(f'write herbs information to excel successfully!')