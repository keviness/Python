from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SwissPrediction/Result1_1/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/OS/Examples/ChangeFIleName/Output/Result1_1/'
SmilesPath = '/Users/kevin/Desktop/program files/python/PythonModules/OS/Examples/ChangeFIleName/Code/SwissSpider.xlsx'
sheetName = 'Result1_1'

def getContents(SmilesPath):
    dataFrame = pd.read_excel(SmilesPath, sheet_name=sheetName)
    data = dataFrame.loc[:, ['MolID','Smiles']].values
    #print('data:\n', data)
    ModuleIDList = data[:,0]
    smilesList = data[:,1]
    #print('smilesList:\n', smilesList)
    return ModuleIDList, smilesList

def changeFileName(inputPath, ModuleIDList):
    os.chdir(inputPath)
    #files = filter(os.path.isfile, os.listdir(inputPath))
    files = os.listdir(inputPath)
    #files.remove(".DS_Store")
    filesList = [os.path.join(inputPath, f) for f in files] 
    #filesList.sort(key=lambda x:int(x.split('SwissTargetPrediction (')[1].split(').csv')[0]))
    # add path to each file
    filesList.sort(key=lambda x: os.path.getmtime(x))
    print('filesList:\n', len(filesList))
    #newest_file = filesList[-1]
    
    for ModuleID, fileName in zip(ModuleIDList, filesList):
        print(f'OldFileName{fileName} -- NewFileName{ModuleID}')
        os.rename(fileName, outputPath+ModuleID+".csv")
    print('filesList Size:\n', len(filesList))

if __name__ == '__main__':
    ModuleIDList, smilesList = getContents(SmilesPath)
    changeFileName(inputPath, ModuleIDList)