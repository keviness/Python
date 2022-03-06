from datetime import date
import pandas as pd
import os
import openpyxl
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/SourceData/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/AverageCaculate/AverageData/ExperimentFilterData/'
averageOutputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FliterData/502HerbsData/502HerbsAverageData/'
HerbPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/AverageCaculate/AverageData/ExperimentHerbsData.xlsx'
sheetName = 'Sheet1'

def getHerbList(HerbPath):
    dataFrame = pd.read_excel(HerbPath, sheet_name=sheetName)
    FZTHerbList = dataFrame['herb'].values
    #print('herbNameList:\n', FZTHerbList)
    return FZTHerbList

def screenExcelFiles(inputPath, FZTHerbList):
    filesNames = os.listdir(inputPath)
    fileHerbNames = [fileName.split('.')[0] for fileName in filesNames]
    i=1
    herbAverageDataFrame = pd.DataFrame()
    screenHerbsList = []
    for herbName in FZTHerbList:
        #herbName = fileName.split('.')[0]
        #postFix = fileName.split('.')[1]
        if herbName not in fileHerbNames:
            continue
        screenHerbsList.append(herbName)
        '''
        if herbName not in fileHerbNames:
            continue
        '''
        print(f'handle herbName:{herbName}')
        #fileName = herbName+'.xlsx'
        #AverageDataFrame = filterData(herbName, i, herbAverageDataFrame)
        filterData(herbName, i , herbAverageDataFrame)
        #print('AverageDataFrame:\n', AverageDataFrame)
        i+=1
    dataFrame = pd.DataFrame(data=screenHerbsList, columns=['herb'])
    dataFrame.to_excel(outputPath+'screenHerbsList.xlsx')
    '''
        herbAverageDataFrame = herbAverageDataFrame.append(AverageDataFrame, ignore_index=True)
        i+=1
    herbAverageDataFrame.set_index('MoleculeName', inplace=True)
    #herbAverageDataFrame.dropna(inplace=True)
    herbAverageDataFrame[['Hdon','Hacc']] = herbAverageDataFrame[['Hdon','Hacc']].round()
    print('herbAverageDataFrame:\n',herbAverageDataFrame)
    herbAverageDataFrame.to_excel(averageOutputPath+'502HerbsPharmacologyAverage1225.xlsx')
    print(f'Write to Excel file Successfully!')
    '''

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
    dataFrame = dataFrame[(dataFrame['DL']>=0.18) & (dataFrame['OB(%)']>=40)].sort_values(by='OB(%)',ascending=False)
    '''
    columnMean = dataFrame[['MW','AlogP','Hdon','Hacc','OB(%)','Caco-2','BBB','DL','FASA-','HL']].mean()
    #columnMean['MolID'] = 'Average'
    #print('columnMean:\n', columnMean)
    #AverageDataFrame['MoleculeName'] = str(index)+herbName
    columnMean['MoleculeName'] = herbName
    dataFrame = dataFrame.append(columnMean, ignore_index=True)
    AverageDataFrame = columnMean
    #print('herbAverageDataFrame:\n', herbAverageDataFrame)
    '''
    dataFrame.to_excel(outputPath+herbName+'.xlsx')
    print(f'Write {index}: {herbName} to Excel file Successfully!')
    #return dataFrame
    
if __name__ == '__main__':
    HerbList = getHerbList(HerbPath)
    screenExcelFiles(inputPath, HerbList)
    