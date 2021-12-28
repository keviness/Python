from datetime import date
from numpy import NaN
import pandas as pd
import os
import openpyxl

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/328HerbsInfo/'

def cleanFZTHerbList(Herbs402Path, Herbs703Path):
    Herbs402dataFrame = pd.read_excel(Herbs402Path)
    Herbs402List = Herbs402dataFrame['Herb name in Chinese'].values
    #print('Herbs402List:\n', Herbs402List)
    #FZTdataFrame.set_index('Herb name in Chinese', inplace=True)
    Herbs703dataFrame = pd.read_excel(Herbs703Path, sheet_name='SimpleDataSet')
    #print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    Herbs502List = Herbs703dataFrame['Herb name in Chinese'].values
    #FZT_TTEdataFrame.set_index('MoleculeName', inplace=True)
    
    #print('Herbs502List:\n', Herbs502List)
    #print('Herbs502dataFrame:\n', Herbs502dataFrame)
    result = pd.DataFrame()
    for HerbName in Herbs402List:
        print('HerbName:\n',HerbName)
        if HerbName in Herbs502List:
            selectHerbInfo = Herbs703dataFrame.loc[Herbs703dataFrame['Herb name in Chinese'].isin([HerbName])]
        else:
            selectHerbInfo = pd.DataFrame({'Herb name in Chinese':[HerbName],'Function':[NaN]})
        print('selectHerbInfo:',selectHerbInfo)
        result = result.append(selectHerbInfo, ignore_index=True)
    print('result:\n', result)
    result.to_excel(outputPath+'502_703HerbInfo.xlsx')
    #return FZTHerbList

if __name__ == '__main__':
    Herbs402Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/502HerbsAverageData/502AverageResult.xlsx'
    Herbs703Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/703HerbsData/703Herbs.xlsx'
    cleanFZTHerbList(Herbs402Path, Herbs703Path)