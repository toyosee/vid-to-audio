import { FiLoader, FiCheckCircle, FiAlertCircle } from 'react-icons/fi';

const ConversionProgress = ({ status, progress, error }) => {
  if (!status) return null;

  const statusConfig = {
    uploading: {
      icon: <FiLoader className="w-6 h-6 animate-spin text-blue-500" />,
      message: 'Uploading file...',
      color: 'text-blue-500'
    },
    converting: {
      icon: <FiLoader className="w-6 h-6 animate-spin text-yellow-500" />,
      message: 'Converting video to MP3...',
      color: 'text-yellow-500'
    },
    complete: {
      icon: <FiCheckCircle className="w-6 h-6 text-green-500" />,
      message: 'Conversion complete!',
      color: 'text-green-500'
    },
    error: {
      icon: <FiAlertCircle className="w-6 h-6 text-red-500" />,
      message: error || 'An error occurred',
      color: 'text-red-500'
    }
  };

  const config = statusConfig[status] || statusConfig.error;

  return (
    <div className="w-full max-w-2xl mx-auto mt-6">
      <div className="bg-white border border-gray-200 rounded-xl p-6 shadow-sm">
        <div className="flex items-center space-x-3">
          {config.icon}
          <span className={`font-medium ${config.color}`}>
            {config.message}
          </span>
        </div>
        {progress && status !== 'complete' && status !== 'error' && (
          <div className="mt-4">
            <div className="w-full bg-gray-200 rounded-full h-2.5">
              <div 
                className="bg-blue-600 h-2.5 rounded-full transition-all duration-300"
                style={{ width: `${progress}%` }}
              ></div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ConversionProgress;