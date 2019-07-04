<template>
  <nav
    class="navbar is-dark"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <router-link
        :to="{ name: 'home' }"
        class="navbar-item is-uppercase"
        href="#"
      >
        Todo
      </router-link>
    </div>

    <div class="navbar-end">
      <template v-if="authenticated">
        <div class="navbar-item">
          connecté !
        </div>
      </template>

      <template v-else>
        <div class="navbar-item">
          pas connecté
        </div>
      </template>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Header',
  computed: mapState([ 'authenticated', 'me' ])
}
</script>
