import pandas as pd
import os
import time

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/OS/Examples/MatchFiles/T2DHerbs/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/OS/Examples/MatchFiles/Output/'
sheetName = ''

def getallfile(inputPath):
    os.chdir(inputPath)
    #files = filter(os.path.isfile, os.listdir(inputPath))
    files = os.listdir(inputPath)
    if '.DS_Store' in files: files.remove(".DS_Store")
    filesList = [os.path.join(inputPath, f) for f in files] 
    for filepath in filesList:
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            fileName = filepath.split('/')[-1]
            herbname = filepath.split('/')[-2]
            if fileName == 'MM symptom.csv':
                print('filePath:\n', filepath)
                Newdir=os.path.join(outputPath, herbname+'.csv')
                os.rename(filepath, Newdir)#重命名
                print(filepath+" has changed as "+Newdir)
            #print('pwd:\n', ())

if __name__ == '__main__':
    getallfile(inputPath)