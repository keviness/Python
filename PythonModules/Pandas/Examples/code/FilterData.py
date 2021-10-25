import pandas as pd
import os
import openpyxl
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/SourceData/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FilterData/'

def screenExcelFiles(inputPath):
    filesNames = os.listdir(inputPath)
    #print('filesNames:\n',filesNames[76])
    i=1
    for fileName in filesNames:
        herbName = fileName.split('.')[0]
        postFix = fileName.split('.')[1]
        if postFix != 'xlsx':
            continue
        print(f'handle herbName:{herbName}')
        filterData(fileName, herbName, i)
        print(f'Write{i}: {herbName} to Excel file Successfully!')
        i+=1


def filterData(fileName, herbName, index):
    #print(f'handle herbName:{herbName}')
    dataFrame = pd.read_excel(inputPath+fileName)
    #print('dataFrame:\n', dataFrame.columns)
    del dataFrame[12]
    del dataFrame['Unnamed: 0']
    #print('dataFrame:\n', dataFrame)
    dataFrame.columns = ['MolID','MoleculeName','MW分子量','AlogP分子疏水性','Hdon可能的氢键供体数目','Hacc可能的氢键受体数目','OB口服生物利用度(%)','Caco-2磁导率','BBB血脑屏障穿透性','DL药物相似性',	'FASA-原子的分数水可及表面积','HL药物半衰期']
    dataFrame.set_index('MolID', inplace=True)
    #print('dataFrame:\n', dataFrame)
    dataFrame.dropna(subset=['HL药物半衰期'], inplace = True)
    #print('dataFrame:\n', dataFrame)
    dataFrame = dataFrame[dataFrame['DL药物相似性']>=0.18].sort_values(by='OB口服生物利用度(%)',ascending=False)
    columnMean = dataFrame[['MW分子量','AlogP分子疏水性','Hdon可能的氢键供体数目','Hacc可能的氢键受体数目','OB口服生物利用度(%)','Caco-2磁导率','BBB血脑屏障穿透性','DL药物相似性',	'FASA-原子的分数水可及表面积','HL药物半衰期']].mean()
    #columnMean['MolID'] = 'Average'
    columnMean['MoleculeName'] = 'Average'
    dataFrame = dataFrame.append(columnMean, ignore_index=True)
    #print('dataFrame:\n', dataFrame)
    dataFrame.to_excel(outputPath+str(index)+herbName+'.xlsx')
    
if __name__ == '__main__':
    screenExcelFiles(inputPath)