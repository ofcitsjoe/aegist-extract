from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
import json

from src.services.llm_service import extract_medical_entities
from src.services.ocr_service import extract_text_from_pdf

app = FastAPI(
    title = "AegisExtract API",
    description = "Privacy-Preserving Medical Document Extractor",
    version = "1.0.0"
)

# ensure our assets directory exists
os.makedirs("assets/temp", exist_ok=True)

@app.post("/extract-medical-entities")
def extract_documents(file : UploadFile = File(...)):
    """
    upload a medical pdf. the system will ocr the document and extract structured entitites using a local
    """

    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="invalid file type. please upload a PDF document.")
    
    temp_file_path = f"assets/temp/{file.filename}"

    try:
        # 1. save the uploaded file locally
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. run the OCR pipeline
        print(f"processing {file.filename}...")
        raw_text = extract_text_from_pdf(temp_file_path)

        # 3. run the LLM pipeline
        json_string_result = extract_medical_entities(raw_text)

        # 4. convert the string back into a python dictionary (json format)
        strutured_data = json.loads(json_string_result)

        return{
            "status" : "success",
            "filename" : file.filename,
            "data" : strutured_data
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the document: {str(e)}")
    
    finally:
        # 5. clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
