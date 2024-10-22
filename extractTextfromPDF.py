import PyPDF2
import re

def pullText(pdfFile):
    reader = PyPDF2.PdfReader(pdfFile, strict=False)
    pdfText = []

    for eachPage in reader.pages:
        content = eachPage.extract_text()
        pdfText.append(content)


    pdfText = " ".join(list(map(lambda x : x.replace("\n", "").strip().replace("{", "(").replace("}", ")"), pdfText)))
    pdfText = list(filter(lambda y : len(y)>0, pdfText.split(" ")))[:15_000]

    words_count = len(pdfText)
    pdfText = " ".join(pdfText)

    return (pdfText, words_count)

print(pullText(r"C:\Users\DILEEP PATCHA\Desktop\Books\Complete MBA For Dummies.pdf")[1])


