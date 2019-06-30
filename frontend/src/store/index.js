import Vue from 'vue'
import Vuex from 'vuex'

import mutations from './mutations'
import * as actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    me: {},
    authenticated: false,
    token: null,
    tasks: []
  },
  actions,
  mutations
})
