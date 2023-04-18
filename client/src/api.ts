import axios, { AxiosInstance } from 'axios';

const apiClient: AxiosInstance = axios.create({
  baseURL: 'https://main-server-airiai.netlify.app/api',
});

export default apiClient;

