from src.services.ocr_service import extract_text_from_pdf

if __name__ == "__main__":
    test_pdf_path = "assets/sample.pdf"
    
    try:
        result = extract_text_from_pdf(test_pdf_path)
        print("\n--- EXTRACTION COMPLETE ---")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")