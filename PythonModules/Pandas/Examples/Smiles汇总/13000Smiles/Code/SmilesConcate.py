import pandas as pd
import os
import openpyxl

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/Smiles汇总/13000Smiles/Data/13000smiles/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/Smiles汇总/13000Smiles/Data/Result/'

def screenExcelFiles(inputPath):
    filesNames = os.listdir(inputPath)
    dataFrameResult = pd.DataFrame()
    for fileName in filesNames:
        dataFrame = pd.read_csv(inputPath+fileName)
        dataFrameResult = dataFrameResult.append(dataFrame)
    print('dataFrameResult:\n', dataFrameResult)
    dataFrameResult.to_excel(outputPath+'Smiles13000.xlsx', index=False)
    print('Write to excel file successfully!')

if __name__ == '__main__':
    screenExcelFiles(inputPath)