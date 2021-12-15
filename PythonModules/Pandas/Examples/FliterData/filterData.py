from datetime import date
import pandas as pd
import os
import openpyxl
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/SourceData/'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/FilterData/'
averageOutputPath = '/Users/kevin/Desktop/program files/python/PythonModules/Pandas/Examples/AverageData/'

def cleanFZTHerbList(FZTHerbPath, FZT_TTEHerbPath):
    FZTdataFrame = pd.read_excel(FZTHerbPath)
    FZTHerbList = FZTdataFrame['Herb name in Chinese'].values
    print('FZTdataFrame:\n', FZTdataFrame)
    FZTdataFrame.set_index('Herb name in Chinese', inplace=True)
    FZT_TTEdataFrame = pd.read_excel(FZT_TTEHerbPath)
    #print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    FZT_TTEHerbList = FZT_TTEdataFrame['MoleculeName'].values
    #FZT_TTEdataFrame.set_index('MoleculeName', inplace=True)
    
    print('FZT_TTEdataFrame:\n', FZT_TTEdataFrame)
    print('FZT_TTEHerbList:\n', FZT_TTEHerbList)

    for FZTHerb in FZTHerbList:
        if FZTHerb in FZT_TTEHerbList:
            continue
        FZTdataFrame.drop(index=FZTHerb, inplace=True)
    FZTdataFrame.to_excel(averageOutputPath+'Experiment.xlsx')
    #return FZTHerbList
