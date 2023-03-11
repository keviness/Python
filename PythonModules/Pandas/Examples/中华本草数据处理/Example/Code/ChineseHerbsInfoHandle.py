import re
import os
import pandas as pd
import numpy as np

inputPath = "/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/中华本草/Result/"
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/RE/Example/Result/'

def cutSetence(filepath, keywordList):
    with open(filepath, "r",encoding="UTF-8",errors="ignore") as f:
        lines = f.readlines()
        f.close()
    #print('lines:\n', lines)
    cutResultArray = []
    for keyword in keywordList:
        singWordList = []
        for line in lines:
            if keyword in line:
                lineList = line.split(keyword)
                if len(lineList)<=1:lineStr = 'NaN'
                else:lineStr = lineList[1][0:-1]
                singWordList.append(lineStr)
        #print('singWordList:\n', singWordList)
        #if 'NaN' in singWordList: singWordList.remove('NaN')
        if len(singWordList) == 1 and singWordList[0]=='NaN': 
            cutResultStr='NaN'
        elif len(singWordList) < 1:
            cutResultStr='NaN'
        else:
            #if len(singWordList)>1: singWordList.remove('\n')
            cutResultStr = singWordList[-1]
            
        cutResultArray.append(cutResultStr)
    #print('cutResultArray:\n', cutResultArray)
    return cutResultArray

def GetHerbInfo(inputPath, wordList):
    files = os.listdir(inputPath)
    if '.DS_Store' in files: files.remove(".DS_Store")
    #filesList = [os.path.join(inputPath, f) for f in files]
    resultArray = [] 
    i = 1
    for fileName in files:
        herbName = fileName.split('.txt')[0].split('_')[1]
        print(f'Handle {i} {herbName}')
        cutResultArray = cutSetence(inputPath+fileName, wordList)
        cutResultArray.insert(0,herbName)
        #print('cutResultArray:\n', cutResultArray)
        resultArray.append(cutResultArray)
        resultCutArray = np.array(resultArray)
        dataFrame = pd.DataFrame({'Herb':resultCutArray[:,0],
                              '性味':resultCutArray[:,1],
                              '归经':resultCutArray[:,2],
                              '功能主治':resultCutArray[:,3]})
        dataFrame.to_excel(outputPath+'newChineseHerbsInfo.xlsx', index=False)
        print(f'Write {herbName} to excel file successfully!')
        i += 1
        
if __name__ == '__main__':
    wordList = ['【性味】','【归经】','【功能主治】','药材基源','【原形态】']
    GetHerbInfo(inputPath, wordList)