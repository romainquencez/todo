<template>
  <div class="columns">
    <div class="column is-half is-offset-one-quarter">
      <div class="box">
        <h2 class="title is-2">
          Edition du profil
        </h2>
        <form>
        <b-field label="Nom :">
            <b-input
            required
            v-model="localUser.last_name"
            placeholder="Nom..."
            />
        </b-field>

        <b-field label="Prénom :">
            <b-input
            required
            v-model="localUser.first_name"
            placeholder="Prénom..."
            />
        </b-field>

        <b-field label="Email :">
            <b-input
            required
            v-model="localUser.email"
            placeholder="Email..."
            type="email"
            />
        </b-field>

        <hr />

        <b-field label="URL de l'API Redmine :">
            <b-input
            v-model="localUser.api_url"
            placeholder="URL..."
            type="url"
            />
        </b-field>

        <b-field label="Clé de l'API Redmine :">
            <b-input
            v-model="localUser.api_key"
            placeholder="Clé..."
            type="password"
            password-reveal
            />
        </b-field>

        <hr />

        <b-button
            @click="editUser"
            icon-left="check"
            class="is-fullwidth is-success"
            :class="{ 'is-loading': isLoading }"
            type="submit"
        >
            Modifier
        </b-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'editUser',
  computed: {
    ...mapState([ 'me' ]),
    localUser () {
      return { ...this.me }
    }
  },
  data () {
    return {
      isLoading: false
    }
  },
  methods: {
    editUser () {
      this.$store.dispatch('updateUser', this.localUser).then(() => {
        this.$toast.open({
          message: 'Profil mis à jour !',
          type: 'is-success'
        })
      }).catch(() => {
        this.$toast.open({
          message: "Une erreur s'est produite.",
          type: 'is-danger'
        })
      })
    }
  }
}
</script>
