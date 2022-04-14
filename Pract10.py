'''
    20CS059
    VRAJ PATEL
'''
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

Uni_result = PdfFileReader(str("D:/Study/PIP(Theory)/20CS059_RESULT_SEM3.pdf"))
print(Uni_result.getDocumentInfo())
print(Uni_result.getNumPages())

for page in Uni_result.pages:
    print(page.extractText())
    PdfFileWriter().addPage(page)

with Path("D:/Study/PIP(Theory)/20CS059_RESULT_SEM3.pdf").open("wb") as output:
    PdfFileWriter().write(output)