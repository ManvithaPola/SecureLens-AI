import easyocr

# Global reader (created only when first needed)
reader = None


def get_reader():
    """
    Initialize EasyOCR only once, when an image is actually uploaded.
    """

    global reader

    if reader is None:
        print("Loading EasyOCR model...")
        reader = easyocr.Reader(
            ['en'],
            gpu=False
        )
        print("EasyOCR model loaded.")

    return reader


def extract_text_from_image(image_path):
    """
    Extract text from an image using EasyOCR.
    """

    reader = get_reader()

    results = reader.readtext(image_path)

    text = ""

    for result in results:
        text += result[1] + "\n"

    return text.strip()