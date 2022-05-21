from selenium import webdriver
import pandas as pd
import os
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SWissADME/Data/502T2DM.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SWissADME/Result/'

'''
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', chrome_options=options)
bor.maximize_window()
'''

options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
options.add_argument("--lang=zh-CN")
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', options=options)

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath)
    data = dataFrame.loc[:, ['name','smiles']].values
    #print('data:\n', data)
    ModuleNameList = data[:,0]
    smilesList = data[:,1]
    #print('ModuleNameList:\n', ModuleNameList)
    return ModuleNameList, smilesList
 
def CrawlHerbInfo(ModuleNameList, smilesList, step):
    bor.get('http://www.swissadme.ch/index.php#')
    for i in range(0, len(smilesList)//step+1):
        #print(f'{i}:{len(smilesList[i*200:(i+1)*200])}:{len(ModuleNameList[i*200:(i+1)*200])}')
        smilsStr = '\n'.join(smilesList[i*step:(i+1)*step])
        #print(str(i)+'smilsStr:\n', smilsStr)

        textArea = bor.find_element_by_xpath('//*[@id="smiles"]')
        textArea.send_keys(smilsStr)
        textAreaText = textArea.get_attribute('innerHTML')
        print('textAreaText:\n', textAreaText)
        runBtn = bor.find_element_by_xpath('//*[@id="submitButton"]')
        runBtn.click()
        downloadBtn = bor.find_element_by_xpath('//*[@id="sib_body"]/div[7]/a[1]')
        downloadBtn.click()
        changeFileName(outputPath, str(i))
    bor.close()

def changeFileName(downloadPath, newName):
    os.chdir(downloadPath)
    files = filter(os.path.isfile, os.listdir(downloadPath))
    files = [os.path.join(downloadPath, f) for f in files] # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    newest_file = files[-1]
    os.rename(newest_file, downloadPath+newName+".csv")

if __name__ == '__main__':
    ModuleNameList, smilesList = getContents(inputPath)
    CrawlHerbInfo(ModuleNameList, smilesList, 30)
    #changeFileName(outputPath, '1')
    '''
    typeList = ['Syndrome','TCMSymptoms','MMSymptoms','Ingredient','Target','Disease']
    for scrawType in typeList:
        #print('typeList.index(scrawType)+1:\n',typeList.index(scrawType)+1)
        CrawlHerbInfo(scrawType, typeList.index(scrawType)+1, herbIDList, herbNameList)
    '''