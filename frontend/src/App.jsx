import { useState } from 'react';
import { convertVideo, downloadFile } from './api/client';
import FileUpload from './components/FileUpload';
import ConversionProgress from './components/ConversionProgress';
import DownloadButton from './components/DownloadButton';
import { FiMusic, FiVideo } from 'react-icons/fi';

function App() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState(null);
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState(null);
  const [conversionResult, setConversionResult] = useState(null);

  const developer = "Elijah Abolaji"; 

  const handleFileAccepted = (acceptedFile) => {
    setFile(acceptedFile);
    setStatus(null);
    setError(null);
    setConversionResult(null);
  };

  const handleRemoveFile = () => {
    setFile(null);
    setStatus(null);
    setError(null);
    setConversionResult(null);
  };

  const handleConvert = async () => {
    if (!file) return;

    setStatus('uploading');
    setProgress(20);
    setError(null);

    try {
      setProgress(50);
      setStatus('converting');
      
      const result = await convertVideo(file);
      
      setProgress(100);
      setStatus('complete');
      setConversionResult(result);
    } catch (err) {
      setStatus('error');
      setError(err.error || 'Conversion failed. Please try again.');
      setProgress(0);
    }
  };

  const handleReset = () => {
    setFile(null);
    setStatus(null);
    setProgress(0);
    setError(null);
    setConversionResult(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <div className="container mx-auto px-4 py-12 max-w-4xl">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <FiVideo className="w-10 h-10 text-blue-600" />
            <FiMusic className="w-10 h-10 text-purple-600" />
          </div>
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            Free Video To MP3 Converter
          </h1>
          <p className="text-lg text-gray-600">
            Extract audio from your videos instantly
          </p>
        </div>

        {/* Main Content */}
        <div className="bg-white rounded-2xl shadow-xl p-8">
          {/* File Upload */}
          <FileUpload 
            onFileAccepted={handleFileAccepted}
            file={file}
            onRemove={handleRemoveFile}
          />

          {/* Convert Button */}
          {file && !conversionResult && (
            <div className="text-center mt-6">
              <button
                onClick={handleConvert}
                disabled={status === 'uploading' || status === 'converting'}
                className="px-8 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {status === 'uploading' || status === 'converting' 
                  ? 'Converting...' 
                  : 'Convert to MP3'
                }
              </button>
            </div>
          )}

          {/* Conversion Progress */}
          <ConversionProgress 
            status={status}
            progress={progress}
            error={error}
          />

          {/* Download Button */}
          {conversionResult && (
            <DownloadButton 
              downloadUrl={downloadFile(conversionResult.output_file)}
              filename={conversionResult.output_file}
              onReset={handleReset}
            />
          )}
        </div>

        {/* Footer */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Supports MP4, AVI, MOV, MKV formats • Max file size: 100MB</p>
          <p className="mt-1">Your files are processed securely and deleted after conversion</p>
          <p className="mt-1"><strong>© {new Date().getFullYear()} | Developed By {developer}</strong></p>
        </div>
      </div>
    </div>
  );
}

export default App;