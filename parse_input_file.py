from get_text_from_word import getTextWord
from get_text_from_excel import getTextExcel
from get_text_from_pdf import getTextPDF


def getTextFrom(path):
    fileFormat = path.split('.')[-1]
    if fileFormat == 'docx':
        return getTextWord(path)
    elif fileFormat == 'doc':
        from get_docx_from_doc import save_as_docx
        save_as_docx(path)
        return getTextWord(path.replace('doc', 'docx'))
    elif fileFormat == 'pdf':
        return getTextPDF(path)
    elif fileFormat == 'xls':
        return getTextExcel(path)
    elif fileFormat == 'xlsx':
        return getTextExcel(path)
    else:
        print("Invalid file extension")
        exit(1)
