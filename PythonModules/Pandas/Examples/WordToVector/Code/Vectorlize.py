from datetime import date
import numpy as np
import pandas as pd
import os
import openpyxl

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/'
sheetName1 = 'Table'
sheetName2 = 'Vector'
def getVectorList(Herbs402Path):
    Herbs402dataFrame = pd.read_excel(Herbs402Path, sheet_name=sheetName1)
    Herbs402List = Herbs402dataFrame['Herb name in Chinese'].values
    #print('Herbs402List:\n', Herbs402List)
    #FZTdataFrame.set_index('Herb name in Chinese', inplace=True)
    VectorDataFrame = pd.read_excel(Herbs402Path, sheet_name=sheetName2)
    #print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    VectorDataList = VectorDataFrame[['入药部位','量化规则','中药']].values
    #FZT_TTEdataFrame.set_index('MoleculeName', inplace=True)
    
    #print('VectorDataList:\n', VectorDataList)
    vectorResult = []
    for element in VectorDataList:
        #print('element[0]:', element[0])
        #print('element[1]:', element[1])
        herbs = element[2].split(',')
        #print('herbs:\n',herbs)
        result = []
        for herb in herbs:
            result.append([element[0], element[1], herb])
        result = np.array(result)
        vectorResult.append(result)
    vectorResult = np.array(vectorResult)
    vectorResultArray = vectorResult[0]
    for i in range(1,vectorResult.size):
        vectorResultArray = np.vstack((vectorResultArray,vectorResult[i]))
    print(vectorResultArray)
    VectorLabel = vectorResultArray[:,0]
    vectorList = vectorResultArray[:,1]
    herbList = vectorResultArray[:,2]
    return Herbs402List, VectorLabel, vectorList, herbList

def VectorLize(Herbs402List, VectorLabel, vectorList, herbList):
    result = []
    for herb in Herbs402List:
        if herb in herbList:
            herbIndex = herbList.tolist().index(herb)
            vectorLa = VectorLabel[herbIndex]
            vector = vectorList[herbIndex]
            result.append([herb, vectorLa, eval(vector)])
        else:
            result.append([herb, np.NaN, np.NaN])
    result = np.array(result)
    dataFrame = pd.DataFrame({'herbName':result[:,0],'Medical Part':result[:,1], 'Vector':result[:,2]})
    dataFrame.to_excel(outputPath+'MedicalPartVector.xlsx')
    print('write to excel successfully!')

if __name__ == '__main__':
    Herbs402Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/402中药信息.xlsx'
    Herbs402List, VectorLabel, vectorList, herbList = getVectorList(Herbs402Path)
    VectorLize(Herbs402List, VectorLabel, vectorList, herbList)