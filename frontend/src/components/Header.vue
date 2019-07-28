<template>
  <nav
    class="navbar is-dark"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <div class="navbar-item">
        <font-awesome-icon
          icon="check"
          class="has-text-success">
        </font-awesome-icon>
      </div>

      <router-link
        :to="{ name: 'home' }"
        class="navbar-item is-uppercase has-text-weight-bold"
      >
        Todo
      </router-link>
    </div>

    <div class="navbar-end">
      <template v-if="authenticated">
        <div class="navbar-item">
          {{ me.username }}
        </div>

        <a
          @click="logOut()"
          class="navbar-item"
        >
          <font-awesome-icon
            icon="sign-out-alt"
            class="">
          </font-awesome-icon>
        </a>
      </template>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Header',
  computed: mapState([ 'authenticated', 'me' ]),
  beforeMount () {
    this.$store.dispatch('getUserInfo')
  },
  methods: {
    logOut () {
      this.$store.dispatch('logout')
    }
  }
}
</script>
