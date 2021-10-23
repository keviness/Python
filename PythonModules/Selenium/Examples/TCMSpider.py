from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
# 对指定的url发起请求
bor.get('https://old.tcmsp-e.com/tcmsp.php')

# 进行标签定位
input_enter = bor.find_element_by_xpath('//*[@id="details-button"]')
input_enter.click()
enter_input = bor.find_element_by_xpath('//*[@id="proceed-link"]')
enter_input.click()
#print('text:\n', bor.page_source)

# 向搜索框中录入关键词
search_label = bor.find_element_by_xpath('//*[@id="inputVarTcm"]')
search_label.send_keys("人参")
search_input = bor.find_element_by_xpath('//*[@id="searchBtTcm"]')
search_input.click()
click_herb = bor.find_element_by_xpath('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[3]/a')
click_herb.click()
#sleep(1)
#bor.quit()
'''
# 点击搜索按钮
btn = bor.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)
'''

'''
service = Service('/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
service.start()
dr = webdriver.Remote(service.service_url)

dr.get('https://www.baidu.com/')

dr.find_element('id', 'kw').send_keys('b站')
dr.find_element('id', 'su').click()
'''