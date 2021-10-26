from datetime import date
import pandas as pd
import os
import openpyxl
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/SourceData/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FilterData/'
averageOutputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/AverageData/'

def cleanFZTHerbList(FZTHerbPath, FZT_TTEHerbPath):
    FZTdataFrame = pd.read_excel(FZTHerbPath)
    FZTHerbList = FZTdataFrame['Herb name in Chinese'].values
    print('FZTdataFrame:\n', FZTdataFrame)
    FZTdataFrame.set_index('Herb name in Chinese', inplace=True)
    FZT_TTEdataFrame = pd.read_excel(FZT_TTEHerbPath)
    #print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    FZT_TTEHerbList = FZT_TTEdataFrame['MoleculeName'].values
    #FZT_TTEdataFrame.set_index('MoleculeName', inplace=True)
    
    print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    print('FZT_TTEHerbList:\n', FZT_TTEHerbList)

    for FZTHerb in FZTHerbList:
        if FZTHerb in FZT_TTEHerbList:
            continue
        FZTdataFrame.drop(index=FZTHerb, inplace=True)
    FZTdataFrame.to_excel(averageOutputPath+'Experiment.xlsx')
    #return FZTHerbList

def getFZTHerbList(FZTHerbPath):
    dataFrame = pd.read_excel(FZTHerbPath)
    FZTHerbList = dataFrame['Herb name in Chinese'].values
    #print('herbNameList:\n', herbNameList)
    return FZTHerbList

def screenExcelFiles(inputPath, FZTHerbList):
    filesNames = os.listdir(inputPath)
    fileHerbNames = [fileName.split('.')[0] for fileName in filesNames]
    i=1
    herbAverageDataFrame = pd.DataFrame()
    for fileName in filesNames:
        herbName = fileName.split('.')[0]
        #postFix = fileName.split('.')[1]
        if herbName not in FZTHerbList:
            continue
        '''
        if herbName not in fileHerbNames:
            continue
        '''
        print(f'handle herbName:{herbName}')
        #fileName = herbName+'.xlsx'
        AverageDataFrame = filterData(fileName, herbName, i, herbAverageDataFrame)
        #print('AverageDataFrame:\n', AverageDataFrame)
        herbAverageDataFrame = herbAverageDataFrame.append(AverageDataFrame, ignore_index=True)
        i+=1
    herbAverageDataFrame.set_index('MoleculeName', inplace=True)
    herbAverageDataFrame.dropna(inplace=True)
    print('herbAverageDataFrame:\n',herbAverageDataFrame)
    herbAverageDataFrame.to_excel(averageOutputPath+'AverageResult.xlsx')
    print(f'Write to Excel file Successfully!')

def filterData(fileName, herbName, index, herbAverageDataFrame):
    dataFrame = pd.read_excel(inputPath+fileName)
    #print('dataFrame:\n', dataFrame.columns)
    del dataFrame[12]
    del dataFrame['Unnamed: 0']
    #print('dataFrame:\n', dataFrame)
    dataFrame.columns = ['MolID','MoleculeName','MW分子量','AlogP分子疏水性','Hdon可能的氢键供体数目','Hacc可能的氢键受体数目','OB口服生物利用度(%)','Caco-2磁导率','BBB血脑屏障穿透性','DL药物相似性',	'FASA-原子的分数水可及表面积','HL药物半衰期']
    dataFrame.set_index('MolID', inplace=True)
    dataFrame.dropna(subset=['HL药物半衰期'], inplace = True)
    #print('dataFrame:\n', dataFrame)
    dataFrame = dataFrame[dataFrame['DL药物相似性']>=0.18].sort_values(by='OB口服生物利用度(%)',ascending=False)
    columnMean = dataFrame[['MW分子量','AlogP分子疏水性','Hdon可能的氢键供体数目','Hacc可能的氢键受体数目','OB口服生物利用度(%)','Caco-2磁导率','BBB血脑屏障穿透性','DL药物相似性',	'FASA-原子的分数水可及表面积','HL药物半衰期']].mean()
    #columnMean['MolID'] = 'Average'
    #print('columnMean:\n', columnMean)
    #AverageDataFrame['MoleculeName'] = str(index)+herbName
    columnMean['MoleculeName'] = herbName
    dataFrame = dataFrame.append(columnMean, ignore_index=True)
    AverageDataFrame = columnMean
    #print('herbAverageDataFrame:\n', herbAverageDataFrame)
    #dataFrame.to_excel(outputPath+str(index)+herbName+'.xlsx')
    print(f'Write {index}: {herbName} to Excel file Successfully!')
    return AverageDataFrame
    
if __name__ == '__main__':
    FZTHerbPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FZTHerbs/402中药信息.xlsx'
    FZT_TTEHerbPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FZTHerbs/402_328AverageResult.xlsx'
    #FZTHerbList = getFZTHerbList(FZTHerbPath)
    #screenExcelFiles(inputPath, FZTHerbList)
    cleanFZTHerbList(FZTHerbPath, FZT_TTEHerbPath)