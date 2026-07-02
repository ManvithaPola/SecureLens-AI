import os
import pdfplumber
import pandas as pd


def extract_text(file_path):
    """
    Extract text from supported document formats.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension == ".txt":
        return extract_txt(file_path)

    elif extension == ".csv":
        return extract_csv(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:
        # Lazy import OCR only when an image is uploaded
        from modules.ocr import extract_text_from_image

        return extract_text_from_image(file_path)

    else:
        raise ValueError("Unsupported file format")


def extract_pdf(file_path):
    """
    Extract text from PDF files.
    """

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_txt(file_path):
    """
    Extract text from TXT files.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def extract_csv(file_path):
    """
    Extract text from CSV files.
    """

    df = pd.read_csv(file_path)

    return df.to_string(index=False)
