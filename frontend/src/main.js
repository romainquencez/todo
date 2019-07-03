import Vue from 'vue'
import '@/plugins'
import store from '@/store'
import router from '@/router'
import App from './App.vue'
import '@/axiosConfig'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app')
