import axios from 'axios';

const API_BASE_URL = 'https://vid-to-audio-production.up.railway.app';
// const API_BASE_URL = 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

export const convertVideo = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await apiClient.post('/convert', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Conversion error:', error);
    throw error.response?.data || { error: 'Conversion failed' };
  }
};

export const convertFromURL = async (url) => {
  try {
    const response = await apiClient.post('/convert-from-url', { url }, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('URL conversion error:', error);
    throw error.response?.data || { error: 'Failed to extract audio from URL' };
  }
};

export const downloadFile = (filename) => {
  return `${API_BASE_URL}/download/${filename}`;
};

export default apiClient;