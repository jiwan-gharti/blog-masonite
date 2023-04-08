import axios from 'axios';

const BASE_BACKEND_URL = import.meta.env.VITE_BASE_URL

const token = localStorage.getItem('blog_secret_key');
console.log(`Bearer ${token}`)

const axiosInstance = axios.create({
    baseURL: BASE_BACKEND_URL,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    timeout: 5000 // milliseconds
  });


export default axiosInstance;