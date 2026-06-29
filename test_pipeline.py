from src.services.ocr_service import extract_text_from_pdf
from src.services.llm_service import extract_medical_entities

if __name__ == "__main__":
    pdf_path = "assets/sample.pdf"

    try:
        raw_text = extract_text_from_pdf(pdf_path)

        structured_data = extract_medical_entities(raw_text)
        print("Extracted structured data:", structured_data)

    except Exception as e:
        print(f"An error occurred: {e}")