# 1. Start with a lightweight version of Python 3.10 on Debian Linux
FROM python:3.10-slim

# 2. Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install system-level C++ dependencies (Tesseract and Poppler)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy only the requirements first to leverage Docker layer caching
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy the rest of the application code
COPY . .

# 8. Expose the port FastAPI will run on
EXPOSE 8000

# 9. The command to start the server when the container boots
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]