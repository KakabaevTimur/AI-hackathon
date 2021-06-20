import pdfplumber

def getTextPDF(path):
    pdf = pdfplumber.open(path)
    page = pdf.pages[0]
    text = page.extract_text()
    pdf.close()
    return text
