import PyPDF2
import docx

def extract_text_from_file(file):

    filename = file.filename

    if filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    else:
        return ""
        