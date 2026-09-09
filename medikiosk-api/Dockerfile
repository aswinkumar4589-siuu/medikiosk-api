# MediKiosk AI — FastAPI microservice
# Hosts: conversational history engine (A), OCR digitization (B),
# summarization (C), AI-suggested-conditions classifier (E)

FROM python:3.11-slim

# --- System dependencies ---
# tesseract-ocr: required for Module B (document digitization)
# tesseract-ocr-hin: Hindi language pack (per bilingual requirement)
# libgl1: required by some OCR/image libs (opencv, pillow-simd, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-hin \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# --- Python dependencies ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- App code ---
COPY ./app ./app

# Render sets $PORT at runtime; default to 8000 for local/other hosts.
# Using 0.0.0.0 so the container is reachable from outside.
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
