from datetime import date
import numpy as np
import pandas as pd
import os
import openpyxl

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/'
sheetName1 = 'FeatureVectorTable'
#sheetName2 = 'Vector'

def getVectorList(Herbs402Path):
    Herbs402dataFrame = pd.read_excel(Herbs402Path, sheet_name=sheetName1)
    Herbs402List = Herbs402dataFrame[['Herb','Function']].values
    #print('Herbs402List:\n', Herbs402List)
    herbs = Herbs402List[:,0]
    DescriptionData = Herbs402List[:,1]
    DescriptionSet = np.array(list(set(DescriptionData)))
    DescriptionVector = np.array([i for i in range(1,len(DescriptionSet)+1)])
    DescriptionVectorRule = np.hstack((DescriptionSet.reshape(DescriptionSet.size, 1), DescriptionVector.reshape(DescriptionVector.size, 1)))
    
    DescriptionSetArray = DescriptionSet.tolist()
    Description402Vector = np.array([DescriptionVector[DescriptionSetArray.index(e)] for e in DescriptionData]).reshape(DescriptionData.size, 1)
    herbs402 = herbs.reshape(herbs.size, 1)
    Description402VectorRule = np.hstack((Herbs402List, Description402Vector))
    #print('DescriptionSet:\n', DescriptionSet.reshape(1,DescriptionSet.size))
    print('DescriptionVectorRule:\n', DescriptionVectorRule)
    print('Description402VectorRule:\n', Description402VectorRule)
    
    return DescriptionVectorRule, Description402VectorRule

def writeToExcel(DescriptionVectorRule, Description402VectorRule):

    dataFrame = pd.DataFrame({'Description':DescriptionVectorRule[:,0],'Description Vector':DescriptionVectorRule[:,1]})
    dataFrame.to_excel(outputPath+'FunctionVector.xlsx')

    dataFrame = pd.DataFrame({'herbName':Description402VectorRule[:,0],'Function':Description402VectorRule[:,1], 'Function Vector':Description402VectorRule[:,2]})
    dataFrame.to_excel(outputPath+'Function402Vector.xlsx')
    print('write to excel successfully!')
    
if __name__ == '__main__':
    Herbs402Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/402中药信息.xlsx'
    DescriptionVectorRule, Description402VectorRule = getVectorList(Herbs402Path)
    writeToExcel(DescriptionVectorRule, Description402VectorRule)
    #Herbs402List, VectorLabel, vectorList, herbList = getVectorList(Herbs402Path)
    #VectorLize(Herbs402List, VectorLabel, vectorList, herbList)