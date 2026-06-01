import pdfplumber
import re
def cleanExtractText(text):
    text=re.sub(r"\s+"," ",text)
    text=re.sub(r"[^\w\s]"," ",text)
    text=text.lower()
    text=re.sub(r"\s+"," ",text)
    
    return text



def text_extract(path):
    text=""
    # 
    with pdfplumber.open(path) as pdf:
        for pages in pdf.pages:
            page_text=pages.extract_text()
        if page_text:
            text+=page_text

    return cleanExtractText(text)

