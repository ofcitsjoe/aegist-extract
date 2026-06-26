from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(path: str) -> str:
    """
    converts a PDF file to images and extracts text from those images using OCR.
    """
    
    print(f"converting {path} to images...  ")

    # 1. convert PDF to a list of PIL images (python imaging library)
    images = convert_from_path(path, dpi=300)

    extracted_text = ""

    print(f"extracting text from {len(images)} images...  ")

    # 2. iterate through each image and extract text using pytesseract
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        extracted_text += text

    return extracted_text