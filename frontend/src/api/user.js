import axios from 'axios'

export default {
  getUserInfo: () => axios.get('/api/users/me/')
}
