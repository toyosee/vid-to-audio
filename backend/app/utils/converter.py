from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import uuid
import yt_dlp
import re
from typing import Optional

def convert_mp4_to_mp3(mp4_path, mp3_path=None):
    """
    Converts an MP4 file to MP3 audio format.
    """
    if not mp3_path:
        mp3_path = os.path.splitext(mp4_path)[0] + ".mp3"
        
    try:
        print(f"Loading video: {mp4_path}")
        with VideoFileClip(mp4_path) as video:
            print("Extracting audio and saving as MP3...")
            video.audio.write_audiofile(mp3_path, bitrate="192k", verbose=False, logger=None)
        print(f"✅ Conversion complete! File saved as: {mp3_path}")
        return mp3_path
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        raise e

def generate_unique_filename(original_filename):
    """Generate a unique filename for uploads"""
    extension = os.path.splitext(original_filename)[1]
    unique_id = str(uuid.uuid4())[:8]
    return f"{unique_id}_{original_filename}"

def download_video_from_url(url: str, output_dir: str) -> str:
    """
    Download video from URL using yt-dlp
    Supports YouTube, Facebook, Vimeo, and many more
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate unique filename
        unique_id = str(uuid.uuid4())[:8]
        output_template = os.path.join(output_dir, f"%(title)s_{unique_id}.%(ext)s")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Download best mp4 available
            'outtmpl': output_template,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'ignoreerrors': True,
            'no_color': True,
            'progress_hooks': [],  # Can add progress hooks here
        }
        
        # Additional options for different platforms
        if 'youtube.com' in url or 'youtu.be' in url:
            ydl_opts.update({
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            })
        elif 'facebook.com' in url:
            ydl_opts.update({
                'format': 'best[ext=mp4]/best',
            })
        elif 'vimeo.com' in url:
            ydl_opts.update({
                'format': 'best[ext=mp4]/best',
            })
        
        print(f"📥 Downloading video from: {url}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'video').replace('/', '_').replace('\\', '_')
            
            # Download the video
            ydl.download([url])
            
            # Find the downloaded file
            downloaded_files = [f for f in os.listdir(output_dir) if f.endswith('.mp4')]
            if downloaded_files:
                # Get the most recently downloaded file
                downloaded_file = max(
                    [os.path.join(output_dir, f) for f in downloaded_files],
                    key=os.path.getctime
                )
                return downloaded_file, video_title
            
        raise Exception("No video file was downloaded")
        
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        raise Exception(f"Failed to download video: {str(e)}")

def extract_audio_from_url(url: str, output_dir: str) -> tuple:
    """
    Complete function: download video from URL and convert to MP3
    """
    try:
        # Step 1: Download video
        video_path, title = download_video_from_url(url, output_dir)
        
        # Step 2: Generate MP3 filename
        mp3_filename = f"{title}.mp3"
        mp3_path = os.path.join(output_dir, mp3_filename)
        
        # Step 3: Convert to MP3
        convert_mp4_to_mp3(video_path, mp3_path)
        
        # Step 4: Clean up - remove video file
        if os.path.exists(video_path):
            os.remove(video_path)
        
        return mp3_path, title
        
    except Exception as e:
        raise e