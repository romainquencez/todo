import axios from 'axios'

export default {
  getUserInfo: () => axios.get('/users/me/'),
  create: user => axios.post('/users/', user),
  update: user => axios.put('/users/' + user.id + '/', user)
}
