import pandas as pd

inputPathFile = '/Users/kevin/Desktop/program files/python/开源数据集/中药药品数据集/ChineseMedicine.json'
ExcelPath = '/Users/kevin/Desktop/program files/python/开源数据集/中药药品数据集/Result/'

def jsonToExcel(ExcelName):
    dataFrame = pd.read_json(inputPathFile)
    dataFrame.to_excel(ExcelName+".xlsx") 
    
    print('Write to Excel file successfully!')

if __name__ == '__main__':
    ExcelName = 'ChineseMedicine'
    jsonToExcel(ExcelName)