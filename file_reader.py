import PyPDF2

def read_pdf(file):
    """Extract text from uploaded PDF file"""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text.strip()

def read_txt(file):
    """Read plain text file"""
    return file.read().decode("utf-8").strip()
