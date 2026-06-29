# AegisExtract API

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)

A privacy-preserving, localized NLP pipeline for extracting structured clinical entities from unstructured medical documents using OCR and constrained LLM generation.

---

## 📋 Table of Contents
1. [About the Project](#-about-the-project)
2. [Architecture](#-architecture)
3. [Tech Stack](#-tech-stack)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Future Improvements](#-future-improvements)
7. [License](#-license)

---

## 🎯 About the Project

Healthcare providers possess vast amounts of unstructured data but are limited by strict data privacy laws (HIPAA/GDPR) that prevent the use of public LLM APIs. **AegisExtract** solves this by providing a fully localized, containerized pipeline that extracts patient data without any information leaving the local environment.

**Key highlights:**
- 🔒 100% local — no data ever leaves your machine
- ⚡ Fast OCR-to-JSON pipeline using Tesseract + Llama 3
- 📄 Handles unstructured medical PDFs out of the box
- 🐳 One command Docker deployment

---

## 🏗️ Architecture

```
PDF Input
    │
    ▼
Tesseract OCR  ──► Raw Text
    │
    ▼
Ollama (Llama 3)  ──► Structured Extraction
    │
    ▼
Pydantic Validation
    │
    ▼
JSON Response (via FastAPI)
```

*The entire pipeline runs locally. No external API calls are made at any stage.*

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10 |
| API Framework | FastAPI |
| OCR Engine | Tesseract (via PyTesseract) |
| LLM Engine | Ollama (Llama 3) |
| Schema Validation | Pydantic |
| Containerization | Docker & Docker Compose |

---

## 🚀 Installation

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- [Git](https://git-scm.com/) installed

### Steps

**1. Clone the repository:**
```bash
git clone https://github.com/ofcitsjoe/aegis-extract-api.git
cd aegis-extract-api
```

**2. Run with Docker:**
```bash
docker-compose up --build
```

**3. Access the API docs:**

Open your browser and go to:
```
http://localhost:8000/docs
```
You will see the Swagger UI — an interactive page where you can test the API without writing any code.

---

## 📝 Usage

Send a POST request to `/extract` with a medical PDF file:

```bash
curl -X POST "http://localhost:8000/extract" \
  -H "accept: application/json" \
  -F "file=@sample_report.pdf"
```

**Example JSON response:**
```json
{
  "patient_name": "John Doe",
  "date_of_birth": "1985-03-22",
  "diagnosis": ["Type 2 Diabetes", "Hypertension"],
  "medications": ["Metformin 500mg", "Lisinopril 10mg"],
  "doctor": "Dr. Sarah Patel"
}
```

---

## 🔭 Future Improvements

- [ ] Implement parallel page processing using `concurrent.futures` for faster OCR on large documents
- [ ] Add support for handwritten note normalization
- [ ] Integrate a vector database (ChromaDB) for document querying and semantic search
- [ ] Add a confidence score per extracted field
- [ ] Build a lightweight frontend dashboard for non-technical users

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.