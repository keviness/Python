from selenium import webdriver
import pandas as pd
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Data/703Herbs.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Result/'

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath)
    data = dataFrame.loc[:, ['Herb_id','Chinese_name']].values
    #print('data:\n', data)
    herbIDList = data[:,0]
    herbNameList = data[:,1]
    #print('herbList:\n', herbList)
    return herbIDList, herbNameList
 
def CrawlHerbInfo(bor, herbName):
    numLabel = bor.find_element_by_xpath('//*[@id="reportTableDiv00"]/div[1]/div[3]/div[1]/span[1]')
    numLabelText = numLabel.get_attribute('innerHTML')
    #print('numLabelHtml:\n', numLabelText)
    num = int(numLabelText.split(' ')[-2])
    
    table = bor.find_element_by_xpath('//*[@id="table"]')
    table_html = table.get_attribute('outerHTML')
    print('table_html:\n', table_html)
    data = pd.read_html(table_html)
    dataFrame = dataFrame.append(data, ignore_index=True)
    #print('dataFrame:\n', dataFrame)
    next_page = bor.find_element_by_xpath('//*[@id="grid"]/div[3]/a[3]')
    next_page_class = next_page.get_attribute('class')
    #print('next_page_class:\n', next_page_class)
    '''
    if next_page_class == 'k-link k-state-disabled':
        break
    else:
        next_page.click()
    '''
    dataFrame.to_excel(outputPath+herbName+'.xlsx')
    print(f'write {herbName} information to excel successfully!')


def main():
    bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
    # 对指定的url发起请求
    bor.get('http://www.symmap.org/detail/SMHB00001')
    CrawlHerbInfo(bor)

if __name__ == '__main__':
    #getContents(inputPath)
    main()