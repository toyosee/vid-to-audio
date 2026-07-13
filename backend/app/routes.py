from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
from pathlib import Path
from datetime import datetime
from .utils.converter import (
    convert_mp4_to_mp3, 
    generate_unique_filename, 
    extract_audio_from_url,
    download_video_from_url
)
from .models import ConversionResponse, URLConversionRequest

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
    allowed_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv'}
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension not in allowed_extensions:
        raise HTTPException(
            400, 
            f"Please upload a valid video file. Supported formats: {', '.join(allowed_extensions)}"
        )
    
    input_path = None
    
    try:
        # Generate unique filename and save uploaded file
        unique_filename = generate_unique_filename(file.filename)
        input_path = UPLOAD_DIR / unique_filename
        
        # Save uploaded file
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Generate output filename
        output_filename = os.path.splitext(unique_filename)[0] + ".mp3"
        output_path = DOWNLOAD_DIR / output_filename
        
        # Convert video to audio
        convert_mp4_to_mp3(str(input_path), str(output_path))
        
        # Clean up uploaded file
        if input_path.exists():
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
        if input_path and input_path.exists():
            try:
                os.remove(input_path)
            except:
                pass
        raise HTTPException(500, f"Conversion failed: {str(e)}")

@router.post("/convert-from-url", response_model=ConversionResponse)
async def convert_from_url(request: URLConversionRequest):
    """Extract audio from a video URL (YouTube, Facebook, Vimeo, etc.)"""
    
    try:
        # Validate URL format
        url = str(request.url)
        supported_domains = ['youtube.com', 'youtu.be', 'facebook.com', 'vimeo.com', 'dailymotion.com']
        
        if not any(domain in url.lower() for domain in supported_domains):
            raise HTTPException(
                400, 
                f"Please provide a URL from a supported platform: {', '.join(supported_domains)}"
            )
        
        # Process the URL
        output_path, title = extract_audio_from_url(url, str(DOWNLOAD_DIR))
        
        # Get the filename from the path
        output_filename = os.path.basename(output_path)
        
        return ConversionResponse(
            success=True,
            message=f"Audio extracted successfully!",
            output_file=output_filename,
            download_url=f"/download/{output_filename}",
            title=title,
            source_url=url
        )
        
    except Exception as e:
        raise HTTPException(500, f"Failed to extract audio from URL: {str(e)}")

@router.get("/download/{filename}")
async def download_file(filename: str):
    """Download converted MP3 file"""
    file_path = DOWNLOAD_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(404, "File not found")
    
    # Get file size for response header
    file_size = file_path.stat().st_size
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
            "Content-Length": str(file_size)
        }
    )

@router.delete("/cleanup")
async def cleanup_files():
    """Clean up old files (optional endpoint)"""
    # Delete files older than 1 hour
    import time
    current_time = time.time()
    deleted_count = 0
    
    for file_path in DOWNLOAD_DIR.glob("*.mp3"):
        if current_time - file_path.stat().st_mtime > 3600:  # 1 hour
            try:
                os.remove(file_path)
                deleted_count += 1
            except:
                pass
    
    return {"message": f"Cleaned up {deleted_count} old files"}

@router.get("/health")
async def health_check():
    return {"status": "healthy"}