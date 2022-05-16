from selenium import webdriver
import pandas as pd
import os
import requests
#from selenium.webdriver.support.select import Select
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/DrugBank/Data/ChainLink.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SYMMAP/Result/'

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath)
    data = dataFrame.loc[:, ['TargetName','ChainLink']].values
    print('data:\n', data)
    TargetNameList = data[:,0]
    ChainLinkList = data[:,1]
    print('herbList:\n', TargetNameList)
    return TargetNameList, ChainLinkList
 
def CrawlHerbInfo(TargetNameList, ChainLinkList):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    for TargetName, ChainLink in zip(TargetNameList, ChainLinkList):
        response = requests.get(ChainLink, headers=headers)
        print('response\n',response.text)
        return
        # ---Syndrome---
    

if __name__ == '__main__':
    TargetNameList, ChainLinkList = getContents(inputPath)
    CrawlHerbInfo(TargetNameList, ChainLinkList)
    