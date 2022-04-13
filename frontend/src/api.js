import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:10005/'
})

export default api;
