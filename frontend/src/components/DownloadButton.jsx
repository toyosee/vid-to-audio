import { FiDownload, FiRefreshCw } from 'react-icons/fi';

const DownloadButton = ({ downloadUrl, filename, onReset }) => {
  if (!downloadUrl) return null;

  return (
    <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mt-6">
      <a
        href={downloadUrl}
        download={filename}
        className="inline-flex items-center px-6 py-3 bg-green-600 text-white font-medium rounded-lg hover:bg-green-700 transition-colors shadow-sm"
      >
        <FiDownload className="w-5 h-5 mr-2" />
        Download MP3
      </a>
      <button
        onClick={onReset}
        className="inline-flex items-center px-6 py-3 bg-gray-100 text-gray-700 font-medium rounded-lg hover:bg-gray-200 transition-colors"
      >
        <FiRefreshCw className="w-5 h-5 mr-2" />
        Convert Another
      </button>
    </div>
  );
};

export default DownloadButton;