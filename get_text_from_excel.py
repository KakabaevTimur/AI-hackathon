import sys
import pandas as pd
from os import path

def getTextExcel(filenameExcel):
    dE= pd.read_excel(filenameExcel)
    lines = dE.to_csv().split('\n')
    return [i.split(',')[1:4] for i in lines]


if __name__ == "__main__":
    path = sys.argv[1]
    fileFormat = path.split('.')[-1]
    if fileFormat == 'xls':
        print(getTextExcel(path))
    # file = open("EXCELTest.txt", "w")
    # file.write(getTextExcel(sys.argv[1]))
    # file.close()
