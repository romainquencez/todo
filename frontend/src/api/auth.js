import axios from 'axios'

export default {
  login (credentials) {
    return axios.post('/api/api-token-auth/', credentials).then(response => response.data)
  },
  requestNewToken (token) {
    return axios.post('/api/api-token-refresh/', token).then(response => response.data.token)
  }
}
