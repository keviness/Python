from datetime import date
import pandas as pd
import os
import openpyxl
from pandas.core.frame import DataFrame
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/328中药信息汇总/data/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/328中药信息汇总/402HerbTargets/'
HerbNameFilePath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/328中药信息汇总/data/402中药信息.xlsx'

def getHerbFileNames():
    HerbNamesDataFrame = pd.read_excel(HerbNameFilePath)
    HerbNames = HerbNamesDataFrame['Herb name in Chinese'].values
    #print('HerbNames:\n', HerbNames)
    dataFrame = pd.DataFrame()
    for HerbName in HerbNames:
        HerbFileName = inputPath + HerbName +'.xlsx'
        herbData = unstackHerbData(HerbFileName)
        dataFrame = dataFrame.append(herbData)
    dataFrame.set_index('Herb Name in Chinese', inplace=True)
    print('dataFrame:\n', dataFrame)
    dataFrame.to_excel(outputPath+'402HerbTargetsInfo.xlsx')
    print('write to excel successfully!')

def unstackHerbData(HerbFileName):
    herbDataFrame = pd.read_excel(HerbFileName)
    del herbDataFrame['Unnamed: 0']
    herbDataFrame.set_index('Unnamed: 0.1', inplace=True)
    #print('herbDataFrame:\n', herbDataFrame)
    herbDataFrame = herbDataFrame.T
    #herbDataFrame.set_index('Herb Name in Chinese', inplace=True)
    #print('herbDataFrameUnsatck:\n', herbDataFrame.columns)
    return herbDataFrame

if __name__ == '__main__':
    getHerbFileNames()