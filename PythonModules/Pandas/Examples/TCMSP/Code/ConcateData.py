import pandas as pd
import os
import openpyxl

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/TCMSP/Data/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/TCMSP/Result/'

def concateDataFrame(inputPath):
    files = os.listdir(inputPath)
    print('files:\n', files)
    dataFrameResult = pd.DataFrame()
    for file in files:
        dataFrame = pd.read_csv(inputPath+file)
        dataFrameResult = dataFrameResult.append(dataFrame)
    print('dataFrameResult:\n', dataFrameResult)
    dataFrameResult.to_excel(outputPath+'TCMSPIngredients.xlsx')
    print('write to excel file successfully!')

if __name__ == '__main__':
    concateDataFrame(inputPath)