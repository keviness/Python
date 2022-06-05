from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SwissPrediction/Data/screenedFormulaInfo(已筛选).xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SwissPrediction/Result1/'
outputPathTest = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SwissPrediction/testPath/'

options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
#options.add_argument("--lang=zh-CN")
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', options=options)

def changeFileName(downloadPath, newName):
    os.chdir(downloadPath)
    files = filter(os.path.isfile, os.listdir(downloadPath))
    filesList = [os.path.join(downloadPath, f) for f in files] 
    # add path to each file
    filesList.sort(key=lambda x: os.path.getmtime(x))
    newest_file = filesList[-1]
    os.rename(newest_file, downloadPath+newName+".csv")

if __name__ == '__main__':
    changeFileName(outputPathTest, '2')