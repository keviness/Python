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
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/中华本草/Result/'

def writeFileToText(content, fileName):
    file = open(outputPath +fileName+'.txt', 'w', encoding='utf-8')
    file.write(content)
    file.close()
    print(f'wrtie {fileName} text successful')

def CrawlHerbInfo(bor):
    # 向搜索框中录入关键词
    i = 7783
    while True:
        table = bor.find_element_by_xpath('//*[@id="mainbox"]/div[1]/div[2]/div[2]')
        table_text = table.get_attribute('innerText')
        #table_html = table.get_attribute('innerHTML')
        #print('table_text:\n', table_text)
        currentHerbName = bor.find_element_by_xpath('//*[@id="mainbox"]/div[1]/div[1]/div[2]/p[3]/span').get_attribute('innerText')
        #print('currentHerbName:\n', currentHerbName)
        #nestBtn = bor.find_element_by_xpath('//*[@id="mainbox"]/div[1]/div[2]/div[1]/div[2]/a[2]')
        #nextHerbName = nestBtn.get_attribute('innerText')
        #print('nextHerbName:\n', nextHerbName)
        writeFileToText(table_text, str(i)+'_'+currentHerbName)
        return
        '''
        if nextHerbName != '阿尔泰扭藿香':
            nestBtn.click()
            i += 1
        else: break
        '''

def main():
    bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver')
# 对指定的url发起请求
    bor.get('http://bencao.quchacha.com/ajA2Zw==.html')
    CrawlHerbInfo(bor)

if __name__ == '__main__':
    main()