import easyocr

# Load model once when the application starts
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_path):
    """
    Extract text from an image using EasyOCR.
    """

    results = reader.readtext(image_path)

    text = ""

    for result in results:
        text += result[1] + "\n"

    return text.strip()