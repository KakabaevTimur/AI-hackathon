import sys
from os import path
from pprint import pprint

import pandas as pd


def GetTextExcel(filenameExcel):
    xl = pd.ExcelFile(filenameExcel)
    for sn in xl.sheet_names:
        frame = xl.parse(sn)
        lines = frame.to_csv().split("\n")
        lists = [i.split(',') for i in lines][:-1]
        skill_i = -1
        for i in range(len(lists[0])):
            if "2" in lists[0][i] and ("Tax" in lists[0][i] or "такс" in lists[0][i]):
                skill_i = i
        return [l[skill_i] for l in lists]

if __name__ == "__main__":
    path = sys.argv[1]
    GetTextExcel(path)
