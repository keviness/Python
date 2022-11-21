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

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/2022中国药典/Result/'

def writeFileToText(content, fileName):
    file = open(outputPath +fileName+'.txt', 'w', encoding='utf-8')
    file.write(content)
    file.close()
    print(f'wrtie {fileName} text successful')

def CrawlHerbInfo(bor, url):
    # 向搜索框中录入关键词
    i = 1
    bor.get(url+str(i))
    while True:
        table = bor.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div[1]')
        table_text = table.get_attribute('innerText')
        #table_html = table.get_attribute('innerHTML')
        #print('table_text:\n', table_text)
        currentHerbName = bor.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div/h3').get_attribute('innerText')
        #print('currentHerbName:\n', currentHerbName)
        writeFileToText(table_text, str(i)+'_'+currentHerbName)
    
        if currentHerbName != '麝香':
            bor.execute_script('window.location=\"'+url+str(i)+'\"')
            i += 1
        else: break

def main():
    bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver')
# 对指定的url发起请求
    url = 'https://www.antpedia.com/?action-pharmdetail-id-'
    CrawlHerbInfo(bor, url)

if __name__ == '__main__':
    main()