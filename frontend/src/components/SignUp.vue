<template>
  <div class="columns">
    <div class="column is-half is-offset-one-quarter">
      <div class="box">
        <h2 class="title is-2">
          Inscription
        </h2>

        <form>
        <b-field label="Nom :">
            <b-input
            required
            v-model="user.last_name"
            placeholder="Nom..."
            />
        </b-field>

        <b-field label="Prénom :">
            <b-input
            required
            v-model="user.first_name"
            placeholder="Prénom..."
            />
        </b-field>

        <b-field label="Email :">
            <b-input
            required
            v-model="user.email"
            placeholder="Email..."
            type="email"
            />
        </b-field>

        <b-field label="Mot de passe :">
            <b-input
            required
            v-model="user.password"
            type="password"
            />
        </b-field>

        <b-field label="Mot de passe (vérification) :">
            <b-input
            required
            v-model="passwordCheck"
            password-reveal
            type="password"
            />
        </b-field>

        <b-button
            @click="signUp"
            icon-left="check"
            :disabled="!buttonEnabled"
            class="is-fullwidth is-success"
            :class="{ 'is-loading': isLoading }"
            type="submit"
        >
            Inscription
        </b-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'signUpForm',
  data () {
    return {
      user: {
        first_name: 'Prénom',
        last_name: 'Nom',
        email: 'test@noreply.com',
        password: 'testmdp'
      },
      passwordCheck: 'testmdp',
      isLoading: false
    }
  },
  computed: {
    buttonEnabled () {
      return (
        this.user.first_name &&
        this.user.last_name &&
        this.user.email &&
        this.user.password &&
        this.passwordCheck &&
        this.user.password === this.passwordCheck)
    }
  },
  methods: {
    signUp () {
      this.$store.dispatch('createUser', this.user).then(() => {
        this.$toast.open({
          message: 'Compte créé avec succès !<br />Vous pouvez maintenant vous connecter.',
          type: 'is-success'
        })
        this.$parent.close()
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
