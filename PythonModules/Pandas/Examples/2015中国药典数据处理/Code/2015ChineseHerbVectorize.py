import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

# ----二，读取文件及文件预处理----
path = "/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/2015中国药典数据处理/Result/2015HerbsProcessResult.xlsx"
sheetName = "ExperimentDataBertVectorize"
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/2015中国药典数据处理/Result/'

# ---load Data and prepare handle---
def getData(path):
    sourceDataFrame = pd.read_excel(path, sheet_name=sheetName)
    #print("sourceDataFrame:\n", sourceDataFrame)
    HerbsArray = sourceDataFrame["Herbs"].values
    contentArray = sourceDataFrame["Functions and Indications"].values
    #print("sentences:\n", contentArray)
    FunctionsArray = sourceDataFrame["Functions"].values
    IndicationsArray = sourceDataFrame["Indications"].values
    PropertyArray = sourceDataFrame['Property'].values
    FlavorArray = sourceDataFrame['Flavor'].values
    MeridianArray = sourceDataFrame['Meridian'].values
    #print("PropertyMediaArray:\n", PropertyMediaArray)
    ToxicityArray = sourceDataFrame['Toxicity'].values
    combStrArray = PropertyArray+'、'+FlavorArray+'、'+MeridianArray
    #print("combArray:\n", combArray)
    combArray = [e.split('、') for e in combStrArray]
    comVocabList = list(set(sum(combArray,[])))
    #print('comVocabList:\n', comVocabList)
    return HerbsArray, PropertyArray,FlavorArray, MeridianArray,ToxicityArray, combStrArray, combArray, comVocabList,FunctionsArray,IndicationsArray, contentArray

def getVector(vocabList, inputSetArray, NameList):
    resultArray = []
    for inputSet in inputSetArray:
        returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
        for word in inputSet:  # 遍历每个词条
            if word in vocabList:  # 如果词条存在于词汇表中，则置1
                returnVec[vocabList.index(word)] = 1
            else:
                print("the word: %s is not in my Vocabulary!" % word)
        resultArray.append(returnVec)
    resultArray = np.array(resultArray)
    print('resultArray:\n', resultArray)
    dataFrame = pd.DataFrame(data=resultArray, columns=vocabList)
    dataFrame=dataFrame[NameList]
    return dataFrame  # 返回文档向量
    
if __name__ == '__main__':
    HerbsArray, PropertyArray,FlavorArray, MeridianArray,ToxicityArray, combStrArray, combArray, comVocabList,FunctionsArray,IndicationsArray, contentArray = getData(path)
    NameList = ['寒','热','温','凉','平','酸','苦','甘','辛','咸','涩','淡','心','肝','胆','脾','胃','肺','肾','大肠','小肠','心包','膀胱','三焦']
    dataFrame = getVector(comVocabList, combArray, NameList)
    dataFrame.insert(0,'Herbs',HerbsArray)
    dataFrame['毒性'] = ToxicityArray
    dataFrame['功能'] = FunctionsArray
    dataFrame['主治'] = IndicationsArray
    dataFrame['功能与主治'] = contentArray
    dataFrame.insert(1,'combStrArray',combStrArray)
    
    print('dataFrame:\n', dataFrame)
    dataFrame.to_excel(outputPath+'2020HerbsInfoVectorize.xlsx', index=False)

    
    