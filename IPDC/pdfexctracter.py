# importing required modules
import PyPDF2
from PyPDF2 import PdfFileReader
# pdf = 'C:/Users/Mardin/OneDrive/Documents/pro-mern-stack.pdf'


def evaluateProposal(pdf):
    titles = ['capital', 'Production capacity', 'job creation', 'technology used',
              'backward and forward linkage', 'land Area', 'Shade Area', '']
    # creating a pdf file object
    pdfFileObj = open(pdf, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # printing number of pages in pdf file
    page_number = len(pdfReader.pages)
    t = '0'
    for page_num in range(page_number):
        page = pdfReader.getPage(page_num)
        t += page.extractText()

    # creating a page object
    pageObj = pdfReader.pages[0]
    suggestions = []
    for i in titles:
        result = t.find(i)
        if result >= 0:
            continue
        else:
            suggestions.append(i)
    return suggestions
