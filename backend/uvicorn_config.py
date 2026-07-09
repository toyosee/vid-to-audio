import uvicorn
import os
from pathlib import Path

# Create necessary directories
UPLOAD_DIR = Path("uploads")
DOWNLOAD_DIR = Path("downloads")
UPLOAD_DIR.mkdir(exist_ok=True)
DOWNLOAD_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("RELOAD", "True").lower() == "true",
        log_level=os.getenv("LOG_LEVEL", "info"),
        access_log=True,
        workers=int(os.getenv("WORKERS", 1)),
    )