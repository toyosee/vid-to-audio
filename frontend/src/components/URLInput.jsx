import { useState } from 'react';
import { FiLink, FiYoutube, FiFacebook, FiPlay, FiX } from 'react-icons/fi';

const URLInput = ({ onSubmit, isLoading, error }) => {
  const [url, setUrl] = useState('');
  const [isValid, setIsValid] = useState(true);

  const validateUrl = (input) => {
    const urlPattern = /^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be|facebook\.com|vimeo\.com|dailymotion\.com)\/.+/;
    return urlPattern.test(input);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateUrl(url)) {
      setIsValid(true);
      onSubmit(url);
    } else {
      setIsValid(false);
    }
  };

  const getPlatformIcon = () => {
    if (url.includes('youtube') || url.includes('youtu.be')) {
      return <FiYoutube className="w-5 h-5 text-red-600" />;
    } else if (url.includes('facebook')) {
      return <FiFacebook className="w-5 h-5 text-blue-600" />;
    } else if (url.includes('vimeo')) {
      return <FiPlay className="w-5 h-5 text-blue-500" />;
    }
    return <FiLink className="w-5 h-5 text-gray-400" />;
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Or paste a video URL
          </label>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              {url ? getPlatformIcon() : <FiLink className="w-5 h-5 text-gray-400" />}
            </div>
            <input
              type="url"
              value={url}
              onChange={(e) => {
                setUrl(e.target.value);
                setIsValid(true);
              }}
              placeholder="https://www.youtube.com/watch?v=... or https://facebook.com/..."
              className={`
                block w-full pl-10 pr-24 py-3 border rounded-lg shadow-sm 
                focus:ring-2 focus:ring-blue-500 focus:border-blue-500
                transition-colors
                ${isValid ? 'border-gray-300' : 'border-red-500 focus:ring-red-500'}
              `}
            />
            <button
              type="submit"
              disabled={isLoading || !url}
              className={`
                absolute right-1 top-1 bottom-1 px-4 rounded-md font-medium
                transition-colors flex items-center gap-2
                ${isLoading 
                  ? 'bg-gray-400 cursor-not-allowed' 
                  : 'bg-blue-600 hover:bg-blue-700 text-white'
                }
              `}
            >
              {isLoading ? (
                <>
                  <span className="animate-spin">⏳</span>
                  Processing
                </>
              ) : (
                'Extract Audio'
              )}
            </button>
          </div>
          {!isValid && (
            <p className="mt-2 text-sm text-red-600 flex items-center gap-1">
              <FiX className="w-4 h-4" />
              Please enter a valid URL from YouTube, Facebook, or Vimeo
            </p>
          )}
          {error && (
            <p className="mt-2 text-sm text-red-600 flex items-center gap-1">
              <FiX className="w-4 h-4" />
              {error}
            </p>
          )}
        </div>

        {/* Supported platforms badge */}
        <div className="flex flex-wrap items-center gap-2 text-xs text-gray-500">
          <span className="font-medium">Supports:</span>
          <span className="px-2 py-1 bg-gray-100 rounded-full">YouTube</span>
          <span className="px-2 py-1 bg-gray-100 rounded-full">Facebook</span>
          <span className="px-2 py-1 bg-gray-100 rounded-full">Vimeo</span>
          <span className="px-2 py-1 bg-gray-100 rounded-full">Dailymotion</span>
          <span className="px-2 py-1 bg-gray-100 rounded-full">And more...</span>
        </div>
      </form>

      {/* URL info display */}
      {url && isValid && !isLoading && (
        <div className="mt-2 text-sm text-gray-500 flex items-center gap-2">
          <span>✓ URL is valid</span>
          <span className="text-gray-300">|</span>
          <span>Click "Extract Audio" to start</span>
        </div>
      )}
    </div>
  );
};

export default URLInput;