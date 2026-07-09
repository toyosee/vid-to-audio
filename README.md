# 🎵 Video to MP3 Converter

A full-stack web application that converts video files (MP4, AVI, MOV, MKV) to MP3 audio format. Built with React + Vite + Tailwind CSS for the frontend and FastAPI + MoviePy for the backend.


## ✨ Features

- **Drag & Drop Upload** - Easy file upload with drag-and-drop support
- **Multiple Formats Support** - Convert MP4, AVI, MOV, MKV, WEBM, FLV, WMV
- **Real-time Progress** - Visual feedback during conversion
- **Instant Download** - Download your MP3 file immediately after conversion
- **Clean UI** - Modern, responsive design with Tailwind CSS
- **API Documentation** - Auto-generated FastAPI docs at `/docs`
- **File Management** - Automatic cleanup of old files

## 🚀 Tech Stack

### Frontend
- **React 18** - UI Framework
- **Vite** - Build tool and development server
- **Tailwind CSS** - Utility-first CSS framework
- **React Dropzone** - Drag-and-drop file upload
- **Axios** - HTTP client for API calls
- **React Icons** - Icon library

### Backend
- **FastAPI** - Modern Python web framework
- **MoviePy** - Video/audio processing
- **Uvicorn** - ASGI server
- **Python-multipart** - File upload handling

## 📋 Prerequisites

- **Python 3.8+** (Backend)
- **Node.js 16+** (Frontend)
- **npm** or **yarn** (Frontend package manager)
- **FFmpeg** (Required for MoviePy)

### Installing FFmpeg

#### macOS
```bash
brew install ffmpeg

Ubuntu/Debian
bash

sudo apt update
sudo apt install ffmpeg

Windows

Download from FFmpeg official website and add to PATH.
🔧 Installation
1. Clone the repository
bash

git clone https://github.com/toyosee/vid-to-audio
cd vid-to-audio

2. Backend Setup
bash

cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p uploads downloads

3. Frontend Setup
bash

cd frontend

# Install dependencies
npm install

# Create .env file (optional)
echo "VITE_API_URL=http://localhost:8000" > .env

🏃 Running the Application
Development Mode
Start Backend Server
bash

cd backend
python run.py
# or
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

The backend will run at: http://localhost:8000
Start Frontend Development Server
bash

cd frontend
npm run dev

The frontend will run at: http://localhost:5173
Production Mode
Build Frontend
bash

cd frontend
npm run build

Run Backend with Production Settings
bash

cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

Using Docker (Optional)
bash

# Build and run with Docker Compose
docker-compose up -d

# Or build individually
docker build -t mp4-to-mp3-backend ./backend
docker run -p 8000:8000 mp4-to-mp3-backend

📁 Project Structure
text

mp4-to-mp3-converter/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── routes.py        # API endpoints
│   │   ├── models.py        # Pydantic models
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── converter.py # MoviePy conversion logic
│   ├── uploads/             # Temporary upload storage
│   ├── downloads/           # Converted files storage
│   ├── requirements.txt
│   ├── run.py              # Uvicorn runner
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.jsx
│   │   │   ├── ConversionProgress.jsx
│   │   │   └── DownloadButton.jsx
│   │   ├── api/
│   │   │   └── client.js   # API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── .gitignore
├── README.md
└── docker-compose.yml

🔌 API Endpoints
Base URL: http://localhost:8000
Method	Endpoint	Description
GET	/	API welcome message
GET	/health	Health check
POST	/convert	Upload and convert video to MP3
GET	/download/{filename}	Download converted MP3 file
GET	/docs	Interactive API documentation (Swagger UI)
GET	/redoc	Alternative API documentation (ReDoc)
DELETE	/cleanup	Clean up old files (optional)
API Usage Examples
Convert Video
bash

curl -X POST "http://localhost:8000/convert" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/video.mp4"

Download Converted File
bash

curl -X GET "http://localhost:8000/download/filename.mp3" \
  -H "accept: audio/mpeg" \
  --output audio.mp3

🎨 UI Components
FileUpload Component

    Drag-and-drop file upload

    File type validation (video formats)

    File size limit (100MB)

    File preview with name and size

ConversionProgress Component

    Upload progress indicator

    Conversion status display

    Error handling with user-friendly messages

DownloadButton Component

    Direct download of converted MP3

    Option to convert another file

🧪 Testing
Backend Testing (Coming Soon)
bash

cd backend
pytest

Frontend Testing (Coming Soon)
bash

cd frontend
npm test

📦 Deployment
Deploy to Production
Backend (PythonAnywhere, Heroku, DigitalOcean, AWS)
bash

# Example for Heroku
heroku create mp4-to-mp3-converter
git push heroku main

Frontend (Vercel, Netlify)
bash

# Build for production
npm run build

# Deploy to Vercel
vercel --prod

# Or Netlify
netlify deploy --prod

Environment Variables
Backend (.env)
env

HOST=0.0.0.0
PORT=8000
RELOAD=False
LOG_LEVEL=info
WORKERS=4
UPLOAD_DIR=uploads
DOWNLOAD_DIR=downloads
MAX_FILE_SIZE=104857600

Frontend (.env)
env

VITE_API_URL=http://your-backend-url.com

🐛 Troubleshooting
Common Issues
1. FFmpeg not found
bash

# Install FFmpeg
# Ubuntu/Debian:
sudo apt-get install ffmpeg

# macOS:
brew install ffmpeg

# Windows: Download from ffmpeg.org and add to PATH

2. CORS errors

Make sure the backend CORS settings include your frontend URL:
python

allow_origins=["http://localhost:5173", "http://localhost:3000"]

3. File upload size limit

Update the max file size in both frontend and backend configurations.
4. Permission errors

Ensure the uploads and downloads directories have write permissions:
bash

chmod 755 uploads downloads

🔒 Security Considerations

    File Validation: Only accepts specified video formats

    File Size Limit: Maximum 100MB upload

    Automatic Cleanup: Files are deleted after conversion

    CORS Configuration: Restrict to allowed origins

    No Persistent Storage: Files are not permanently stored

📈 Performance

    Concurrent Conversions: Multiple users can convert simultaneously

    File Size: Handles files up to 100MB

    Conversion Speed: Depends on video length and hardware

    Memory Usage: Optimized with MoviePy's streaming capabilities

🤝 Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

Development Guidelines

    Follow PEP 8 for Python code

    Use ESLint and Prettier for JavaScript/React

    Write meaningful commit messages

    Update documentation when adding features

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

    FastAPI - Excellent Python framework

    MoviePy - Video editing library

    React - UI library

    Tailwind CSS - Utility-first CSS

    Vite - Next-generation frontend tooling

📞 Support

For support, email tyabolaji@gmail.com or open an issue on GitHub.
🗺️ Roadmap

    Batch file conversion

    Audio quality selection

    Progress tracking with WebSockets

    Audio preview before download

📊 Statistics

    Supported Video Formats: 7+

    Max File Size: 100MB

    Conversion Time: ~30 seconds for 100MB video

    API Response Time: < 100ms

Built using React, FastAPI, and MoviePy
text


# Contributing to MP4 to MP3 Converter

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Process

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Code Style

### Python
- Follow PEP 8
- Use type hints
- Document functions with docstrings

### JavaScript/React
- Use ESLint with standard configuration
- Use functional components and hooks
- Use PropTypes or TypeScript

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the docs with any new environment variables
3. The PR will be merged once you have the sign-off of at least one maintainer