from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
import os
from pathlib import Path

# Create directories if they don't exist
UPLOAD_DIR = Path("uploads")
DOWNLOAD_DIR = Path("downloads")
UPLOAD_DIR.mkdir(exist_ok=True)
DOWNLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(
    title="MP4 to MP3 Converter API",
    description="Convert video files to MP3 audio format",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "https://mp3-grab.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "MP4 to MP3 Converter API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "mp4-to-mp3-converter"}