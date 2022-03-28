from selenium import webdriver

import pandas as pd
url = 'https://old.tcmsp-e.com/molecule.php?qn='
bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')

#options = webdriver.WebKitGTKOptions()
#prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': '默认下载路径'} 
#options.add_experimental_option('prefs', prefs)

bor.get(url)
input_enter = bor.find_element_by_xpath('//*[@id="details-button"]')
input_enter.click()
enter_input = bor.find_element_by_xpath('//*[@id="proceed-link"]')
enter_input.click()
path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP502/selectMol.xlsx'

def getMolList(path):
    dataFrame = pd.read_excel(path)
    MolList = dataFrame['SelectMol'].values
    idList = [mol.split('L')[1] for mol in MolList]
    print('idList:\n', idList)
    return idList
    
def crawlMold(idList):
    for id in idList:
        bor.get(url+id)
        # 对指定的url发起请求
        imgBtn = bor.find_element_by_xpath('//*[@id="container_lsp"]/div[2]/table/thead/tr[3]/td/a/img')
        imgBtn.click()
        print(f'Mol{id} download successfully!')
    bor.close()
    
if __name__ == '__main__':
    idList = getMolList(path)
    crawlMold(idList)