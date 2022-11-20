import pandas as pd
import os
import openpyxl

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Result/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/TCMSP-ComTarget/Data/'

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

if __name__ == '__main__':
    concateDataFrame(inputPath)