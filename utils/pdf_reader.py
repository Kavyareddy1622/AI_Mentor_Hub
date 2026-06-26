from pypdf import PdfReader


def extract_text(pdf_file):
    """
    Extract text from an uploaded PDF.
    """
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text