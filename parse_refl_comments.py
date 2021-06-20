import sys
from pprint import pprint

import pandas as pd

import words


def GetTextExcel(filenameExcel):
    df = pd.read_excel(filenameExcel)
    mylist = df['REFLEXION_2'].tolist()
    text = ""
    for line in mylist:
        text += line
    text = words.clear_text(text)
    return text

def getComments(path = None):
    if path == None:
        path = sys.argv[1]
    return GetTextExcel(path)
