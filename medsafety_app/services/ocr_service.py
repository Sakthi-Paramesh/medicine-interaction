import pytesseract
from PIL import Image

# If tesseract is not in your PATH, you may need to point to the executable:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_file):
    try:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        raise Exception(f"Failed to extract text: {str(e)}")
