from selenium import webdriver
import pandas as pd

path = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/PubChem/html.txt'
options = webdriver.ChromeOptions()
# 设置参数
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
#options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')  
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
options.add_argument("--lang=zh-CN")
#options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')
bor = webdriver.Chrome(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/chromedriver', options=options)
jsText = open('/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/Code/stealth.min.js', 'r').read()
bor.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    # 这里的操作大概就是把控制台中的window.navigator.webdriver =undefined  赋值   因为人机操作会认为是Ture
        "source": '''Object.defineProperties(navigator,webdriver:{get:()=> undefined}'''
    })
bor.maximize_window()
#bor = webdriver.Edge(executable_path='/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Source/msedgedriver')
# 对指定的url发起请求
bor.get('https://pubchem.ncbi.nlm.nih.gov/#query=beta-sitosterol')
#print('text:\n', bor.page_source)
'''
with open(path, 'w') as f:
    f.write(bor.page_source)
    f.close()
'''
# 进行标签定位
SMILES_html = bor.find_element_by_class_name('p-xsm-top p-xsm-bottom inline-block')
#print('SMILES_html:\n', SMILES_html[0].text)
result = SMILES_html.get_attribute('innerHTML')
print('result:\n', result)

bor.close()