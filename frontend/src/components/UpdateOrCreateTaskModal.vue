<template>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">
        {{ task.id ? 'Edition' : 'Création' }} d'une tâche
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
        @click="updateOrCreateTask()"
        :value="task.id ? 'Modifier' : 'Créer'" />
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
    updateOrCreateTask () {
      this.$store.dispatch(
        this.localTask.id ? 'updateTask' : 'createTask',
        this.localTask
      ).then(() => {
        this.$toast.open({
          message: this.localTask.id ? 'Tâche éditée !' : 'Tache créée !',
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
