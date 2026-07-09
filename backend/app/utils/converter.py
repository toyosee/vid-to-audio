from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import uuid

def convert_mp4_to_mp3(mp4_path, mp3_path=None):
    """
    Converts an MP4 file to MP3 audio format.
    """
    # Auto-generate MP3 filename if not provided
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