<template>
  <section class="hero is-fullheight is-login-page">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div
          class="column has-background-black-ter"
          v-if="!authenticated"
        >
          <h3 class="title has-text-white is-size-1">
            Todo
        </h3>
          <p class="subtitle has-text-white has-text-centered">
            Pour accéder au formulaire de demande, merci de bien vouloir vous connecter.
          </p>
          <div class="form">
            <form @submit.prevent="submit">
              <b-field label="Identifiant">
                <b-input v-model="username">
                </b-input>
              </b-field>
              <b-field label="Mot de passe">
                <b-input
                  required
                  v-model="password"
                  type="password"
                >
                </b-input>
              </b-field>
              <button
                class="button is-block has-background-success has-text-white is-fullwidth is-uppercase"
                type="submit"
              >
                Se connecter
              </button>
            </form>
          </div>
        </div>
        <div
          class="column is-authentified"
          v-else
        >
          <h4>
            Vous êtes déjà authentifié.
          </h4>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Auth from '@/api/auth'
import { mapState } from 'vuex'

export default {
  name: 'login',
  data () {
    return {
      username: null,
      password: null
    }
  },
  computed: mapState([ 'authenticated' ]),
  methods: {
    logIn (username, password) {
      Auth.login({
        username: this.username,
        password: this.password
      }).then(response => {
        this.$store.dispatch('login', { token: response.token })
        this.$router.push(this.$route.query.redirect || { name: 'home' })
      })
    },
    submit () {
      this.logIn(
        this.username,
        this.password)
    }
  }
}
</script>
