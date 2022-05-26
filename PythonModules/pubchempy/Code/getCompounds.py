from unittest import result
import urllib
import pubchempy
import pandas as pd
import numpy as np
from sqlalchemy import true
import time
inputPath = '/Users/kevin/Desktop/program files/python/PythonModules/pubchempy/Data/502Ingredients.xlsx'
outputPath = '/Users/kevin/Desktop/program files/python/PythonModules/pubchempy/Result/'

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