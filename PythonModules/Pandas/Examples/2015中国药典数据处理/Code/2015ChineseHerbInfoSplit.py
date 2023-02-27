import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

# ----二，读取文件及文件预处理----
path = "/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/2015中国药典数据处理/Result/2015ChineseHerbsInfo.xlsx"
sheetName = "ExperimentData"
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/2015中国药典数据处理/Result/'

# ---load Data and prepare handle---
def getData(path):
    sourceDataFrame = pd.read_excel(path, sheet_name=sheetName)
    #print("sourceDataFrame:\n", sourceDataFrame)
    HerbsArray = sourceDataFrame["Herb"].values
    contentArray = sourceDataFrame["功能与主治"].values
    #print("sentences:\n", contentArray)
    PropertyMediaArray = sourceDataFrame['性味与归经'].values
    #print("PropertyMediaArray:\n", PropertyMediaArray)
    PropertyMediaArray = [e[0:-1].strip() for e in PropertyMediaArray]
    #print("MediaArray:\n", PropertyMediaArray)
    PropertyArray = np.array([e.split('。')[0] for e in PropertyMediaArray])
    #print("PropertyArray:\n", PropertyArray)
    MediaArray = []
    for ele in PropertyMediaArray:
        eleStrList = ele.split('。')
        if len(eleStrList)<=1: estr = 'NaN'
        else: estr = eleStrList[1]
        MediaArray.append(estr)
    MediaArray = np.array(MediaArray)
    print("MediaArray:\n", MediaArray)
    return HerbsArray, PropertyMediaArray, PropertyArray, MediaArray,contentArray

def splitPropertyFlavour(PropertyArray):
    FlavourArray = [e.split('，')[0] for e in PropertyArray]
    FlavourArray = np.array(FlavourArray)
    print('FlavourArray:\n', FlavourArray)
    toxicityHotColdArray = []
    for ele in PropertyArray:
        eleStrList = ele.split('，')
        if len(eleStrList)<=1: estr = 'NaN'
        else: estr = eleStrList[1]
        toxicityHotColdArray.append(estr)
    HotColdArray = np.array([e.split('；')[0] for e in toxicityHotColdArray])
    print("HotColdArray:\n", HotColdArray)
    toxicityHotColdArray = np.array(toxicityHotColdArray)
    toxicityArray = []
    for ele in PropertyArray:
        eleStrList = ele.split('；')
        if len(eleStrList)<=1: estr = '无毒'
        else: estr = eleStrList[1]
        toxicityArray.append(estr)
    toxicityArray = np.array(toxicityArray)
    print("toxicityArray:\n", toxicityArray)
    return HotColdArray, FlavourArray, toxicityArray

def splitFunctionZhuZhi(contentArray):
    FunctionArray = [e[0:-1].split('。')[0] for e in contentArray]
    FunctionArray = np.array(FunctionArray)
    print('FunctionArray:\n', FunctionArray)
    ZhuZhiArray = []
    for ele in contentArray:
        eleStrList = ele.split('。')
        if len(eleStrList)<=1: estr = 'NaN'
        else: estr = eleStrList[1]
        ZhuZhiArray.append(estr)
    ZhuZhiArray = np.array(ZhuZhiArray)
    print("ZhuZhiArray:\n", ZhuZhiArray)
    return FunctionArray, ZhuZhiArray

def PropertyDataFrame(HerbsArray,PropertyMediaArray,HotColdArray, FlavourArray, toxicityArray, MediaArray,FunctionArray, ZhuZhiArray,contentArray):
    dataFrame = pd.DataFrame({'Herbs':HerbsArray,
                              'Property&Meridian&Toxicity':PropertyMediaArray,
                              'Property':HotColdArray,
                              'Flavor':FlavourArray,
                              'Toxicity':toxicityArray,
                              'Meridian':MediaArray,
                              'Functions':FunctionArray,
                              'Indications':ZhuZhiArray,
                              'Functions and Indications':contentArray})
    dataFrame.to_excel(outputPath+'2015HerbsProcessResult.xlsx',index=False)
    print('write to Excel file successfully!')

def getVector(vocabList, inputSetArray):
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
    print('resultArray:\n', resultArray.shape)
    dataFrame = pd.DataFrame(data=resultArray, columns=vocabList)
    dataFrame=dataFrame[['寒','热','温','凉','酸','苦','甘','辛','咸','心','肝','胆','脾','胃','肺','肾','大肠','小肠','心包','膀胱','三焦', '毒']]
    #print('dataFrame:\n', dataFrame)
    return dataFrame  # 返回文档向量
    
if __name__ == '__main__':
    HerbsArray, PropertyMediaArray, PropertyArray, MediaArray,contentArray = getData(path)
    HotColdArray, FlavourArray, toxicityArray = splitPropertyFlavour(PropertyArray)
    FunctionArray, ZhuZhiArray = splitFunctionZhuZhi(contentArray)
    PropertyDataFrame(HerbsArray, PropertyMediaArray, HotColdArray, FlavourArray, toxicityArray, MediaArray,FunctionArray, ZhuZhiArray,contentArray)
    
    