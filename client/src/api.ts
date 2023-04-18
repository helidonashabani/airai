import axios, { AxiosInstance } from 'axios';

const apiClient: AxiosInstance = axios.create({
  baseURL: 'https://main--main-server-airiai.netlify.app/api',
});

export default apiClient;
