import axios from 'axios'

const BASE_URL = '/api/tasks/'

export default {
  get: task => axios.get(BASE_URL),
  create: task => axios.post(BASE_URL, task),
  update: task => axios.put(BASE_URL + task.id + '/', task),
  delete: task => axios.delete(BASE_URL + task.id + '/', task)
}
