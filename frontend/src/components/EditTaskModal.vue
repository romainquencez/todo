<template>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">
        Edition
      </p>
    </header>

    <section class="modal-card-body">
      <b-field label="Titre">
        <b-input
          required
          v-model="localTask.name"
        />
      </b-field>

      <b-field label="Description">
        <b-input
          v-model="localTask.description"
          type="textarea"
        />
      </b-field>

      <b-field label="Numéro de ticket">
        <b-input
          type="number"
          v-model="localTask.issue"
        />
      </b-field>

      <b-field label="Résolue ?">
        <b-checkbox
          type="is-success"
          v-model="localTask.done"
        ></b-checkbox>
      </b-field>
    </section>

    <footer class="modal-card-foot">
      <input
        class="button is-primary"
        type="button"
        @click="updateTask()"
        value="Modifier" />
      <input
        class="button is-danger is-outlined"
        type="button"
        @click="$parent.close()"
        value="Annuler" />
    </footer>
  </div>
</template>

<script>
export default {
  name: 'EditTaskModal',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  computed: {
    localTask () {
      return { ...this.task }
    }
  },
  methods: {
    updateTask () {
      this.$store.dispatch('updateTask', this.localTask).then(() => {
        this.$toast.open({
          message: 'Tâche éditée !',
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
