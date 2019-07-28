import * as types from './mutation-types'

export default {
  [types.LOGIN] (state) {
    state.authenticated = true
  },
  [types.LOGOUT] (state) {
    state.authenticated = false
    state.token = null
  },
  [types.SET_TOKEN] (state, { token }) {
    state.token = token
  },
  [types.SET_USER_INFO] (state, { user }) {
    state.me = user
  },
  [types.UPDATE_USER] (state, user) {
    state.me = user
  },
  [types.SET_TASKS] (state, { tasks }) {
    state.tasks = tasks
  },
  [types.CREATE_TASK] (state, { task }) {
    state.tasks.push(task)
  },
  [types.UPDATE_TASK] (state, { task }) {
    state.tasks.splice(
      state.tasks.findIndex(item => item.id === task.id),
      1,
      task
    )
  },
  [types.DELETE_TASK] (state, { task }) {
    state.tasks.splice(
      state.tasks.findIndex(item => item.id === task.id),
      1
    )
  }
}
