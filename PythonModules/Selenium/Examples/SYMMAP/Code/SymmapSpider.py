from selenium import webdriver
import pandas as pd
import os
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Data/703Herbs.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Result/'
#bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
'''
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', chrome_options=options)
bor.maximize_window()
'''
#options = webdriver.WebKitGTKOptions()
#prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '默认下载路径'} 
#options.add_experimental_option('prefs', prefs)

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath)
    data = dataFrame.loc[:, ['Herb_id','Chinese_name']].values
    #print('data:\n', data)
    herbIDList = data[:,0]
    herbNameList = data[:,1]
    #print('herbList:\n', herbList)
    return herbIDList, herbNameList
 
def CrawlHerbInfo(downLoadType, btnIndex, herbIDList, herbNameList):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath+downLoadType+'/'}
    options.add_experimental_option('prefs', prefs)
    bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', chrome_options=options)
    bor.maximize_window()
    for herbID in len(zip(herbIDList, herbNameList)):
        #print(f'{herbID}:{herbName}')
        bor.get('http://www.symmap.org/detail/SMHB'+str(herbID+1))
        # ---Syndrome---
        SyndromeBtn = bor.find_element_by_xpath('//*[@id="button_select_group"]/button['+str(btnIndex)+']')
        SyndromeBtn.click()
        downloadBtn = bor.find_element_by_xpath('//*[@id="dl-btn"]')
        downloadBtn.click()
        #changeFileName(outputPath+downLoadType, str(herbID)+herbName+downLoadType)
    bor.close()
    
def changeFileName(downloadPath, newName):
    os.chdir(downloadPath)
    files = filter(os.path.isfile, os.listdir(downloadPath))
    files = [os.path.join(downloadPath, f) for f in files] # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    newest_file = files[-1]
    os.rename(newest_file, newName+".csv")

if __name__ == '__main__':
    herbIDList, herbNameList = getContents(inputPath)
    typeList = ['Syndrome','TCMSymptoms','MMSymptoms','Ingredient','Target','Disease']
    for scrawType in typeList:
        #print('typeList.index(scrawType)+1:\n',typeList.index(scrawType)+1)
        CrawlHerbInfo(scrawType, typeList.index(scrawType)+1, herbIDList, herbNameList)
    