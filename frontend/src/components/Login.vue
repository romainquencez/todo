<template>
  <div class="columns">
    <div class="column is-half is-offset-one-quarter">
      <div class="box">
        <h2 class="title is-2">
          Connexion
        </h2>

        <template v-if="!authenticated">
          <form>
            <b-field label="Identifiant">
              <b-input
                icon="user"
                required
                v-model="username"
              />
            </b-field>
            <b-field label="Mot de passe">
              <b-input
                icon="key"
                required
                v-model="password"
                type="password"
              />
            </b-field>
            <b-button
              @click="logIn"
              class="is-fullwidth is-primary"
              :class="{ 'is-loading': isLoading }"
              type="submit"
            >
              Se connecter
            </b-button>
          </form>
        </template>

        <template v-else>
          <p>
            Vous êtes déjà connecté.
          </p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import Auth from '@/api/auth'
import { mapState } from 'vuex'

export default {
  name: 'login',
  data () {
    return {
      username: null,
      password: null,
      isLoading: false
    }
  },
  computed: mapState([ 'authenticated' ]),
  methods: {
    logIn () {
      this.isLoading = true
      Auth.login({
        username: this.username,
        password: this.password
      }).then(response => {
        this.$store.dispatch('login', { token: response.token })
        this.$router.push(this.$route.query.redirect || { name: 'home' })
      }).catch(() => {
        this.$dialog.alert({
          title: "Erreur d'authentification",
          message: 'Les informations saisies ne correspondent à aucun utilisateur.',
          type: 'is-danger',
          hasIcon: true,
          icon: 'times-circle'
        })
      }).finally(this.isLoading = false)
    }
  }
}
</script>
