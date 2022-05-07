from selenium import webdriver
import pandas as pd
import os
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Data/703Herbs.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Result/'
#bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': outputPath}
options.add_experimental_option('prefs', prefs)
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', chrome_options=options)
bor.maximize_window()
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
 
def CrawlHerbInfo(bor, herbIDList, herbNameList):
    for herbID, herbName in zip(herbIDList, herbNameList):
        #print(f'{herbID}:{herbName}')
        bor.get('http://www.symmap.org/detail/SMHB'+str(herbID))
        SyndromeBtn = bor.find_element_by_xpath('//*[@id="button_select_group"]/button[1]')
        SyndromeBtn.click()
        downloadPath = outputPath+herbName
        os.makedirs(downloadPath)
        prefs['download.default_directory'] = downloadPath
        downloadBtn = bor.find_element_by_xpath('//*[@id="dl-btn"]')
        downloadBtn.click()
        prefs['download.default_directory'] = downloadPath
    '''
    numLabel = bor.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div[1]/span')
    numLabelText = numLabel.get_attribute('innerHTML')
    #print('numLabelHtml:\n', numLabelText)
    num = int(numLabelText.strip().split(' ')[-2])
    #print('num:\n', num)
    dataFrame = pd.DataFrame()
    for i in range(1, (num//10)+1):
        table = bor.find_element_by_xpath('//*[@id="table"]')
        table_html = table.get_attribute('outerHTML')
        #print('table_html:\n', table_html)
        data = pd.read_html(table_html)
        dataFrame = dataFrame.append(data, ignore_index=True)
        #print('dataFrame:\n', dataFrame)
        next_page_btn = bor.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div[2]/ul/li[9]/a')
        next_page_btn.click()
        #print('next_page_class:\n', next_page_class)
    dataFrame.to_excel(outputPath+herbName+'.xlsx')
    print(f'write {herbName} information to excel successfully!')
    '''

if __name__ == '__main__':
    herbIDList, herbNameList = getContents(inputPath)
    CrawlHerbInfo(bor, herbIDList, herbNameList)
    bor.close()
    #main()