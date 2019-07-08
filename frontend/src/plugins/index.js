import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import {
  faUser, faKey, faTimesCircle, faCheck, faSignOutAlt, faExclamation
} from '@fortawesome/free-solid-svg-icons'
import { dom, library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.use(Buefy, {
  defaultIconPack: 'fas'
})

// Font Awesome

dom.watch()

library.add(faUser, faKey, faTimesCircle, faCheck, faSignOutAlt, faExclamation)

Vue.component('font-awesome-icon', FontAwesomeIcon)
