import pandas as pd
import os
import time

inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Selenium/Examples/SwissPrediction/Result/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/OS/Examples/ChangeFIleName/Output/Result/'
sheetName = ''

def changeFileName(inputPath):
    os.chdir(inputPath)
    #files = filter(os.path.isfile, os.listdir(inputPath))
    files = os.listdir(inputPath)
    #files.remove(".DS_Store")
    filesList = [os.path.join(inputPath, f) for f in files] 
    #filesList.sort(key=lambda x:int(x.split('SwissTargetPrediction (')[1].split(').csv')[0]))
    # add path to each file
    filesList.sort(key=lambda x: os.path.getmtime(x))
    print('filesList:\n', len(filesList))
    #newest_file = filesList[-1]

if __name__ == '__main__':
    changeFileName(inputPath)