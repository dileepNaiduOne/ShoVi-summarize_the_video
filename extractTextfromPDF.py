import PyPDF2
import re

def pullText(pdfFile):
    with open(pdfFile, 'rb') as file:
        reader = PyPDF2.PdfReader(file, strict=False)
        pdfText = []

        for eachPage in reader.pages:
            content = eachPage.extract_text()
            pdfText.append(content)


    pdfText = " ".join(list(map(lambda x : x.replace("\n", "").strip(), pdfText)))
    pdfText = list(filter(lambda y : len(y)>0, pdfText.split(" ")))[:20_00_000]

    words_count = len(pdfText)
    pdfText = " ".join(pdfText)

    return (pdfText, words_count)

# print(pullText(r"f.pdf"))


