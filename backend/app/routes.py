from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
from pathlib import Path
from .utils.converter import convert_mp4_to_mp3, generate_unique_filename
from .models import ConversionResponse

router = APIRouter()

# Create directories if they don't exist
UPLOAD_DIR = Path("uploads")
DOWNLOAD_DIR = Path("downloads")
UPLOAD_DIR.mkdir(exist_ok=True)
DOWNLOAD_DIR.mkdir(exist_ok=True)

@router.post("/convert", response_model=ConversionResponse)
async def convert_video(file: UploadFile = File(...)):
    """Convert MP4 to MP3"""
    
    # Validate file type
    if not file.filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
        raise HTTPException(400, "Please upload a valid video file (MP4, AVI, MOV, MKV)")
    
    try:
        # Generate unique filename and save uploaded file
        unique_filename = generate_unique_filename(file.filename)
        input_path = UPLOAD_DIR / unique_filename
        
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Generate output filename
        output_filename = os.path.splitext(unique_filename)[0] + ".mp3"
        output_path = DOWNLOAD_DIR / output_filename
        
        # Convert video to audio
        convert_mp4_to_mp3(str(input_path), str(output_path))
        
        # Clean up uploaded file
        os.remove(input_path)
        
        return ConversionResponse(
            success=True,
            message="Conversion successful!",
            input_file=file.filename,
            output_file=output_filename,
            download_url=f"/download/{output_filename}"
        )
        
    except Exception as e:
        # Clean up on error
        if input_path.exists():
            os.remove(input_path)
        raise HTTPException(500, f"Conversion failed: {str(e)}")

@router.get("/download/{filename}")
async def download_file(filename: str):
    """Download converted MP3 file"""
    file_path = DOWNLOAD_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(404, "File not found")
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="audio/mpeg"
    )

@router.get("/health")
async def health_check():
    return {"status": "healthy"}