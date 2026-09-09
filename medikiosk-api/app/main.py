"""
MediKiosk AI — FastAPI microservice entrypoint.

Route groups (fill in as you build each module per the build order):
  /history/*   -> Module A: conversational history engine
  /ocr/*       -> Module B: document digitization
  /summarize   -> Module C: structured history summary generator
  /predict     -> Module E: AI-suggested probable conditions

Ping /health right before a demo to wake up a sleeping free-tier
Render instance ahead of time.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="MediKiosk AI Service")

# --- CORS ---
# Restrict this to your actual Vercel domain before submission.
# "*" is fine for local dev only.
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    """Used for uptime checks and pre-demo wake-up pings."""
    return {"status": "ok"}


# --- Route registration ---
# As you build each module, create an APIRouter in its own file
# (e.g. app/routers/history.py) and include it here, e.g.:
#
# from app.routers import history, ocr, summarize, predict
# app.include_router(history.router, prefix="/history", tags=["history"])
# app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])
# app.include_router(summarize.router, tags=["summarize"])
# app.include_router(predict.router, tags=["predict"])
