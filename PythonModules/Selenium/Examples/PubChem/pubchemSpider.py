from selenium import webdriver
import pandas as pd

path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/PubChem/html.txt'
bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
# 对指定的url发起请求
bor.get('https://pubchem.ncbi.nlm.nih.gov/#query=beta-sitosterol')
#print('text:\n', bor.page_source)
with open(path, 'w') as f:
    f.write(bor.page_source)
    f.close()
# 进行标签定位
'''
SMILES_html = bor.find_element_by_xpath('///*[@id="collection-results-container"]/div/div/div[2]/ul/li[1]/div/div/div[1]/div[2]/div[3]')
#print('SMILES_html:\n', SMILES_html[0].text)
result = SMILES_html.get_attribute('innerHTML')
print('result:\n', result)
'''
bor.close()