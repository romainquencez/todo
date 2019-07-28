import Auth from '@/api/auth'
import User from '@/api/user'
import Task from '@/api/tasks'

import * as types from './mutation-types'
import router from '@/router'

// Auth

export const login = ({ commit }, payload) => {
  commit(types.SET_TOKEN, payload)
  commit(types.LOGIN)
}

export const logout = ({ commit }) => {
  commit(types.LOGOUT)
  router.push({ name: 'login' })
}

export const refreshToken = ({ commit, state }) => {
  const token = state.token
  if (token) {
    Auth.requestNewToken({ token })
      .then(newToken => commit(types.SET_TOKEN, { token: newToken }))
      .catch(() => commit(types.LOGOUT))
  }
}

// User

export const getUserInfo = ({ commit, state }) => {
  return User.getUserInfo().then(response => {
    commit(types.SET_USER_INFO, { user: response.data })
  })
}

export const createUser = ({ commit, state }, user) => {
  return User.create(user).then(response => response)
}

// Task

export const getTasks = ({ commit }) => {
  return Task.get().then(response => {
    commit(types.SET_TASKS, { tasks: response.data })
  })
}

export const createTask = ({ commit }, task) => {
  return Task.create(task).then(response => {
    commit(types.CREATE_TASK, { task: response.data })
  })
}

export const updateTask = ({ commit }, task) => {
  return Task.update(task).then(response => {
    commit(types.UPDATE_TASK, { task: response.data })
  })
}

export const deleteTask = ({ commit }, task) => {
  return Task.delete(task).then(response => {
    commit(types.DELETE_TASK, { task: response.data })
  })
}
