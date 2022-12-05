import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

# ----二，读取文件及文件预处理----
CHineseHerb2022Path = "/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/2022中国药典(在中华本草中药)/Data/2022中国药典Herbs.xlsx"
ChineseHerbZHBCPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/2022中国药典(在中华本草中药)/Data/ChineseHerbsFull.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/2022中国药典(在中华本草中药)/Result/'

# ---load Data and prepare handle---
def getScreenData():
    ChineseHerb2022DataFrame = pd.read_excel(CHineseHerb2022Path)
    print("ChineseHerb2022DataFrame:\n", ChineseHerb2022DataFrame)
    Herbs2022Array = ChineseHerb2022DataFrame["Herbs"].values
    ChineseHerbZHBCDataFrame = pd.read_excel(ChineseHerbZHBCPath)
    ZHBCHerbsArray = ChineseHerbZHBCDataFrame["Herb"].values
    ChineseHerbZHBCDataFrame.set_index('Herb',inplace=True)
    #print("ChineseHerbZHBCDataFrame:\n", ChineseHerbZHBCDataFrame)
    screenHerbArray = []
    for herb in Herbs2022Array:
        if herb in ZHBCHerbsArray:
            screenHerbArray.append(herb)
    screenedZHBCDataFrame = ChineseHerbZHBCDataFrame.loc[screenHerbArray,:]
    print('screenedZHBCDataFrame:\n', screenedZHBCDataFrame)
    
    screenedZHBCDataFrame.to_excel(outputPath+'screenedZHBCResult.xlsx')
    print('Write to excel file successfully!')

    
if __name__ == '__main__':
    getScreenData()
    #dataFrame = getVector(combSetArray, combListArray)
    #print('dataFrame:\n', dataFrame)
    #PropertyDataFrame(HerbsArray, PropertyArray, MediaArray,contentArray)
    