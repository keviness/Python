from datetime import date
import pandas as pd
import os
import openpyxl
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/SourceData/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/502HerbsPharmacology/'
averageOutputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/502HerbsAverageData/'
HerbPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/AverageCaculate/AverageData/328中药信息.xlsx'
sheetName = 'Table'

def getHerbList(HerbPath):
    dataFrame = pd.read_excel(HerbPath, sheet_name=sheetName)
    FZTHerbList = dataFrame['Herb Name'].values
    print('herbNameList:\n', FZTHerbList)
    return FZTHerbList

def screenExcelFiles(inputPath, FZTHerbList):
    filesNames = os.listdir(inputPath)
    fileHerbNames = [fileName.split('.')[0] for fileName in filesNames]
    i=1
    herbAverageDataFrame = pd.DataFrame()
    for herbName in FZTHerbList:
        #herbName = fileName.split('.')[0]
        #postFix = fileName.split('.')[1]
        if herbName not in fileHerbNames:
            continue
        '''
        if herbName not in fileHerbNames:
            continue
        '''
        print(f'handle herbName:{herbName}')
        #fileName = herbName+'.xlsx'
        AverageDataFrame = filterData(herbName, i, herbAverageDataFrame)
        #print('AverageDataFrame:\n', AverageDataFrame)
        herbAverageDataFrame = herbAverageDataFrame.append(AverageDataFrame, ignore_index=True)
        i+=1
    herbAverageDataFrame.set_index('MoleculeName', inplace=True)
    #herbAverageDataFrame.dropna(inplace=True)
    herbAverageDataFrame[['Hdon','Hacc']] = herbAverageDataFrame[['Hdon','Hacc']].round()
    print('herbAverageDataFrame:\n',herbAverageDataFrame)
    herbAverageDataFrame.to_excel(averageOutputPath+'502HerbsPharmacologyAverage1225.xlsx')
    print(f'Write to Excel file Successfully!')

def filterData(herbName, index, herbAverageDataFrame):
    dataFrame = pd.read_excel(inputPath+herbName+'.xlsx')
    #print('dataFrame:\n', dataFrame.columns)
    del dataFrame[12]
    del dataFrame['Unnamed: 0']
    #print('dataFrame:\n', dataFrame)
    dataFrame.columns = ['MolID','MoleculeName','MW','AlogP','Hdon','Hacc','OB(%)','Caco-2','BBB','DL',	'FASA-','HL']
    dataFrame.set_index('MolID', inplace=True)
    dataFrame.dropna(subset=['HL'], inplace = True)
    #print('dataFrame:\n', dataFrame)
    dataFrame = dataFrame[(dataFrame['DL']>=0.5) & (dataFrame['OB(%)']>=35)].sort_values(by='OB(%)',ascending=False)
    columnMean = dataFrame[['MW','AlogP','Hdon','Hacc','OB(%)','Caco-2','BBB','DL','FASA-','HL']].mean()
    #columnMean['MolID'] = 'Average'
    #print('columnMean:\n', columnMean)
    #AverageDataFrame['MoleculeName'] = str(index)+herbName
    columnMean['MoleculeName'] = herbName
    dataFrame = dataFrame.append(columnMean, ignore_index=True)
    AverageDataFrame = columnMean
    #print('herbAverageDataFrame:\n', herbAverageDataFrame)
    dataFrame.to_excel(outputPath+str(index)+herbName+'.xlsx')
    print(f'Write {index}: {herbName} to Excel file Successfully!')
    return AverageDataFrame
    
if __name__ == '__main__':
    HerbList = getHerbList(HerbPath)
    screenExcelFiles(inputPath, HerbList)
    