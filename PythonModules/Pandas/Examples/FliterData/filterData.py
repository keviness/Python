from datetime import date
from numpy import NaN
import pandas as pd
import os
import openpyxl

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/328HerbsInfo/'

def cleanFZTHerbList(Herbs502Path, Herbs703Path):
    Herbs502dataFrame = pd.read_excel(Herbs502Path)
    Herbs502List = Herbs502dataFrame['Herb name in Chinese'].values
    #print('Herbs402List:\n', Herbs402List)
    #FZTdataFrame.set_index('Herb name in Chinese', inplace=True)
    Herbs703dataFrame = pd.read_excel(Herbs703Path, sheet_name='Table')
    #print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    Herbs703List = Herbs703dataFrame['Herb'].values
    #FZT_TTEdataFrame.set_index('MoleculeName', inplace=True)
    
    #print('Herbs502List:\n', Herbs502List)
    #print('Herbs502dataFrame:\n', Herbs502dataFrame)
    result = pd.DataFrame()
    for HerbName in Herbs502List:
        print('HerbName:\n',HerbName)
        if HerbName in Herbs703List:
            selectHerbInfo = Herbs703dataFrame.loc[Herbs703dataFrame['Herb'].isin([HerbName])]
        else:
            selectHerbInfo = pd.DataFrame({'Herb':[HerbName],'Function':[NaN]})
        #print('selectHerbInfo:',selectHerbInfo)
        result = result.append(selectHerbInfo, ignore_index=True)
    #print('result:\n', result)
    result.to_excel(outputPath+'502_402HerbInfo.xlsx', index=False)
    print('write to excel file successfully!')
    #return FZTHerbList

if __name__ == '__main__':
    Herbs502Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/502Herbs.xlsx'
    Herbs703Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/402中药信息.xlsx'
    cleanFZTHerbList(Herbs502Path, Herbs703Path)