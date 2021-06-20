import re
import os
import win32com.client as win32
from win32com.client import constants

from glob import glob
paths = glob('M:\Hackathon\data\\**\\*.doc', recursive=True)

def save_as_docx(path):
    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)
    if not os.path.isfile(new_file_abs):
        # Opening MS Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(path)
        doc.Activate()
        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)

if __name__ == "__main__":
    for path in paths:
        print(path)
        save_as_docx(path)
