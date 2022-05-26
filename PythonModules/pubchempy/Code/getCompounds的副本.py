from unittest import result
import urllib
import pubchempy
import pandas as pd
import numpy as np
from sqlalchemy import true
import time
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/pubchempy/Data/502Ingredients.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/pubchempy/Result/'
'''
with open('D:\ame.txt','r',encoding='utf-8-sig') as file1:
    file_lines = file1.readlines()
    name_list=[]
    a=[]
    cc=[]
    d=[]
    e=[]
    f=[]
    g=[]
#readlines读取的每行是字符串格式，采用以下代码将其转换成列表格式
    for i in file_lines:
        j=i.strip() #去掉每行头尾空白
        name_list.append(str(j))
    for k in  name_list:
        results = pubchempy.get_compounds(k, 'name')
        for l in results:
            try:
                print('CID: {}\tMass: {}\tName: {}\tMolfor: {}\tSmi: {}\tSyn: {}'.format(l.cid,l.exact_mass,l.iupac_name,l.molecular_formula,l.isomeric_smiles,l.synonyms))
                MFs=l.molecular_formula
                MWs=l.molecular_weight
                ISs=l.isomeric_smiles
                Sys=l.synonyms
                Cis=l.cid
                a.append(k)
                cc.append(MFs)
                d.append(ISs)
                e.append(Sys)
                f.append(Cis)
                g.append(MWs)
            except (pubchempy.BadRequestError, TimeoutError, urllib.error.URLError,ValueError):
                pass
            dataframe=pd.DataFrame({'name':a,'molecular_formula':cc,'molecular_weight':g,'smiles':d,'synonyms':e,'cid':f})
            dataframe.to_csv ("D://imput.csv",index=False,sep=',')
'''

def getContents(inputPath):
    dataFrame = pd.read_excel(inputPath,sheet_name='Sheet1')
    data = dataFrame.loc[:, ['ChemID','Molecule Name']].values
    #print('data:\n', data)
    ChemIDList = data[:,0]
    MoleculeNameList = data[:,1]
    #print('ModuleNameList:\n', MoleculeNameList)
    return ChemIDList, MoleculeNameList

def getCompoundsInfo(ChemIDList, MoleculeNameList):
    compoundList = []
    molecular_formulasList = []
    isomeric_smilesList = []
    CidsList = []
    chemIDList = []
    i = 0
    for chemID, molecule in list(zip(ChemIDList, MoleculeNameList)):
        #print('ChemID:', chemID)
        compoundsResults = pubchempy.get_compounds(molecule, namespace='name')
        #print('compoundsResults:\n', compoundsResults)
        #compoundsResults.to_excel(outputPath+"result.xlsx")
        for compound in compoundsResults:
            #print('CID: {}\tMass: {}\tName: {}\tMolfor: {}\tSmi: {}\tSyn: {}'.format(compound.cid,compound.exact_mass,compound.iupac_name,compound.molecular_formula, compound.isomeric_smiles, compound.synonyms))
            molecular_formulas=compound.molecular_formula
            #MWs=compound.molecular_weight
            isomeric_smiles=compound.isomeric_smiles
            #synonyms=compound.synonyms
            Cids=compound.cid
            chemIDList.append(chemID)
            compoundList.append(molecule)
            molecular_formulasList.append(molecular_formulas)
            isomeric_smilesList.append(isomeric_smiles)
            CidsList.append(Cids)
            
            dataframe=pd.DataFrame({'ChemID':chemIDList,
                                    'CompoundName':compoundList, 
                                    'molecular_formula':molecular_formulasList,
                                    'smiles':isomeric_smilesList,
                                    'cid':CidsList})
            dataframe.to_excel(outputPath+"SmilesResult.xlsx",index=False)
            print(f'{i}-{chemID}:{molecule} write to excel file successfully!')
        i += 1
        time.sleep(3)
        
if __name__ == '__main__':
    ChemIDList, MoleculeNameList = getContents(inputPath)
    getCompoundsInfo(ChemIDList, MoleculeNameList)