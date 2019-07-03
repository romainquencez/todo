import axios from 'axios'
import store from '@/store'

axios.defaults.baseURL = '/api'

axios.interceptors.request.use(
  config => {
    const token = store.state.token
    if (token) {
      config.headers.Authorization = `JWT ${token}`
    }
    return config
  },
  error => Promise.reject(error)
)
