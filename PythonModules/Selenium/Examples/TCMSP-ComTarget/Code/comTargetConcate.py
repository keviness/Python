import pandas as pd
import os
import openpyxl

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Result/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Data/'
filePath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Data/TCMSPComponentTargets.xlsx'
fileOutputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Result/fileOutputPath/'

def concateDataFrame(inputPath):
    files = os.listdir(inputPath)
    #print('files:\n', files)
    if '.DS_Store' in files: files.remove('DS_Store')
    
    dataFrameResult = pd.DataFrame()
    for file in files:
        dataFrame = pd.read_excel(inputPath+file)
        dataFrameResult = dataFrameResult.append(dataFrame)
    del dataFrameResult['Unnamed: 0']
    print('dataFrameResult:\n', dataFrameResult)
    dataFrameResult.to_excel(outputPath+'TCMSPComponentTargets.xlsx',index=False)
    print('write to excel file successfully!')
    #return dataFrameResult

def dataGroupBy(filePath):
    dataFrame = pd.read_excel(filePath)
    print('dataFrame:\n', dataFrame)
    groupDataframes = dataFrame.groupby(['MOLID','MoleculeName'])
    print('groupDataframes:\n', groupDataframes)
    resultArray = []
    for name, group in groupDataframes:
        print('name:\n', name)
        targetStr = ';'.join(group['target'].values)
        print('targetStr:\n', targetStr)
        resultArray.append([name[0],name[1],targetStr])
    print('resultArray:\n', resultArray)
    resultDataFrame = pd.DataFrame(data = resultArray, columns=['MolID','ComponentName','Targets'])
    print('resultDataFrame:\n', resultDataFrame)
    resultDataFrame.to_excel(fileOutputPath+'TCMSPCompTargets.xlsx',index=False)
    print('write to excel file successfully!')
    
if __name__ == '__main__':
    #concateDataFrame(inputPath)
    dataGroupBy(filePath)