# from src.resume_to_text import text_extract

# path=input("Enter file path")
# print(text_extract(path))

import pdfplumber
path=input("Enter path")
with pdfplumber.open(path,password=None) as pdf:
    text=""
    for page in pdf.pages:
        text+=page.extract_text()
    print(text)