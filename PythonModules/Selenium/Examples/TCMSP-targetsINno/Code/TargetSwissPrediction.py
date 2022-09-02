from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time
import shutil
import random
from fake_useragent import UserAgent


inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-targetsINno/Data/concateComponentsSmiles.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-targetsINno/Result'
outputCachePath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-targetsINno/ResultCache/'
notTargetMolPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-targetsINno/notTargetMol/'
sheet_name = 'ScreenData507'
proxy_list = [
'218.255.162.95:553'
]
proxy = random.choice(proxy_list)
UserAgent = UserAgent().random

options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
#options.add_argument("--lang=zh-CN")
options.add_argument('user-agent='+UserAgent)
#options.add_argument('--proxy-server=http://' + proxy)

#prefs0 = {"profile.managed_default_content_settings.images":2}
#options.add_experimental_option("prefs",prefs0)
prefs = {"profile.managed_default_content_settings.images":2,
         'profile.default_content_settings.popups': 0, 
         'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)

#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', options=options)

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath, sheet_name=sheet_name)
    data = dataFrame.loc[:, ['ChemID','smiles']].values
    #print('data:\n', data)
    ModuleIDList = data[:,0]
    smilesList = data[:,1]
    print('ModuleIDList:\n', ModuleIDList)
    print('smilesList:\n', smilesList)
    return ModuleIDList, smilesList

def CrawlHerbInfo(ModuleIDList, smilesList):
    bor.get('http://www.swisstargetprediction.ch/')
    notMolID = []
    notSmiles = []
    i = 1
    for molID, smilesStr in zip(ModuleIDList, smilesList):
        print("process:{} {}---{}".format(i, molID, smilesStr))
        #print(str(i)+'smilsStr:\n', smilsStr)
        smilesBox = bor.find_element_by_xpath('//*[@id="smilesBox"]')
        smilesBox.send_keys(smilesStr)
        smilesBox.send_keys(Keys.ENTER)
        '''
        runBtn = bor.find_element_by_xpath('//*[@id="submitButton"]')
        runBtn.click()
        '''
        try:
            downloadBtn = bor.find_element_by_xpath('//*[@id="exportButtons"]/div/button[2]')
        except:
            print(f'{i}  {molID}---{smilesStr} do not have targets!')
            bor.execute_script("window.location='http://www.swisstargetprediction.ch/'")
            notMolID.append(molID)
            notSmiles.append(smilesStr)
            dataFrame = pd.DataFrame(data={'molID':notMolID, 'smiles':notSmiles})
            dataFrame.to_excel(notTargetMolPath+'notTargetMol.xlsx')
            continue
            #time.sleep(2)
        else:
            downloadBtn.click()
            print("{} {}--{}Download successfully!".format(i, molID, smilesStr))
            #changeFileName(outputPath, molID)
            bor.execute_script("window.location='http://www.swisstargetprediction.ch/'")
            CopyFileName(outputPath, outputCachePath, molID)
        time.sleep(random.randint(1,10))
        i += 1
    bor.close()

def changeFileName(denstPath, newName):
    os.chdir(denstPath)
    files = filter(os.path.isfile, os.listdir(denstPath))
    filesList = [os.path.join(denstPath, f) for f in files] 
    # add path to each file
    filesList.sort(key=lambda x: os.path.getmtime(x))
    newest_file = filesList[-1]
    os.rename(newest_file, denstPath + newName+ ".csv")

def CopyFileName(downloadPath, newFilePath, newName):
    os.chdir(downloadPath)
    files = filter(os.path.isfile, os.listdir(downloadPath))
    filesList = [os.path.join(downloadPath, f) for f in files] 
    # add path to each file
    filesList.sort(key=lambda x: os.path.getmtime(x))
    newest_file = filesList[-1]
    
    if os.path.exists(newFilePath):
        shutil.copy(newest_file, newFilePath)
        changeFileName(newFilePath, newName)
    else:
        print('目的文件夹不存在，无法复制')

if __name__ == '__main__':
    ModuleIDList, smilesList = getContents(inputPath)
    CrawlHerbInfo(ModuleIDList, smilesList)
    #changeFileName(outputPathTest, '2')
    #CopyFileName(outputPath, outputPathTest, 'test1')