import axios from 'axios';

const API_BASE_URL = 'https://vid-to-audio-production.up.railway.app';

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

export const downloadFile = (filename) => {
  return `${API_BASE_URL}/download/${filename}`;
};

export default apiClient;