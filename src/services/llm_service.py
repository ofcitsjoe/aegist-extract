import ollama
from pydantic import BaseModel, Field

class MedicalRecord(BaseModel):
    patient_age: int | None = Field(description="The age of the patient. Return null if not found.")
    primary_diagnoses: list[str] = Field(description="The main current medical conditions or reasons for assessment.")
    past_medical_history: list[str] = Field(description="Previous or chronic medical conditions (e.g., hypertension, heart problems, past strokes).")
    social_history: str | None = Field(description="Brief summary of the patient's living situation, marital status, and employment.")
    medications: list[str] = Field(description="List of prescribed medications and dosages.")

def extract_medical_entities(text:str) -> str:
    """
    passes raw OCR text to Llama 3 and enforces a strict JSON schema output
    """

    print("initialising local LLM inference...  ")

    prompt = f"""
    You are an expert medical data extractor. Extract the required information from the following medical document.

    Document:
    {text}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}],
        format=MedicalRecord.model_json_schema(), # this enforces a strict JSON schema output
        options={'temperature':0} # 0 guarantees the most deterministic, factual output
    )

    return response['message']['content']  # return the extracted medical entities in JSON format