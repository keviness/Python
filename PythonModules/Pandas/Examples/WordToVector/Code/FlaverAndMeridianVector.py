from datetime import date
import numpy as np
import pandas as pd
import os
import openpyxl

outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/'
sheetName1 = 'FeatureVectorTable'
sheetName2 = 'Vector'
FlavorDic = {'酸':1,'苦':2,'甘':3,'辛':4,'咸':5,'涩':6,'淡':7}
MeridianDic = {'肝经':1,'心经':2,'脾经':3,'肺经':4,'胃经':5,'胆经':6,'肾经':7,'小肠经':8,'大肠经':9,'三焦经':10,'膀胱经':11,'心包经':12}

def getHerbInfoVector(Herbs402Path):
    Herbs402dataFrame = pd.read_excel(Herbs402Path, sheet_name=sheetName1)
    HerbsInfoList = Herbs402dataFrame[['Herb','Herb Meridian Tropism','Herb Flavor']].values

    #herbs = HerbsInfoList[:,0]
    HerbMeridianTropism = HerbsInfoList[:,[0,1]]
    HerbFlavor = HerbsInfoList[:,[0,2]]
    HerbMeridianTropismResultArray = getVectorList(HerbMeridianTropism, MeridianDic)
    HerbFlavorResultArray = getVectorList(HerbFlavor, FlavorDic)
    #print('HerbMeridianTropism:\n', HerbMeridianTropism)
    #print('HerbFlavor:\n', HerbFlavor)
    print('HerbFlavorData:\n', HerbFlavorResultArray)
    return HerbMeridianTropismResultArray, HerbFlavorResultArray
    
def getVectorList(HerbsInfoArray, infoDic):
    HerbsInfoResultArray = []
    for HerbsInfo in HerbsInfoArray:
        infoList = HerbsInfo[1].split(',')
        herbResult = transToVector(infoList, infoDic)
        HerbsInfoResultArray.append([HerbsInfo[0],HerbsInfo[1],herbResult])
    HerbsInfoResultArray = np.array(HerbsInfoResultArray)
    
    return HerbsInfoResultArray
    
def transToVector(infoList, infoDic):
    HerbInfoArray = []
    herbResult = 0
    for info in infoList:
        HerbInfoArray.append(infoDic.get(info))
    #print('HerbInfoArray:\n', HerbInfoArray)
    
    for i in range(len(HerbInfoArray)):
        index = pow(0.1, i)
        herbResult += index*HerbInfoArray[i]
    #print('herbResult:\n', herbResult)
    return round(herbResult, 6)

def writeToExcel(HerbMeridianTropismResultArray, HerbFlavorResultArray):

    dataFrame = pd.DataFrame({'Herb Name':HerbMeridianTropismResultArray[:,0],'Herb Meridian Tropism':HerbMeridianTropismResultArray[:,1], 'Vector':HerbMeridianTropismResultArray[:,2]})
    dataFrame.to_excel(outputPath+'HerbMeridianTropism402Vector.xlsx')

    dataFrame = pd.DataFrame({'herbName':HerbFlavorResultArray[:,0],'Herb Flavor':HerbFlavorResultArray[:,1], 'Function Vector':HerbFlavorResultArray[:,2]})
    dataFrame.to_excel(outputPath+'HerbFlavor402Vector.xlsx')
    print('write to excel successfully!')
    
if __name__ == '__main__':
    Herbs402Path = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/WordToVector/Data/402中药信息.xlsx'
    HerbMeridianTropismResultArray, HerbFlavorResultArray = getHerbInfoVector(Herbs402Path)
    #DescriptionVectorRule, Description402VectorRule = getVectorList(Herbs402Path)
    writeToExcel(HerbMeridianTropismResultArray, HerbFlavorResultArray)
