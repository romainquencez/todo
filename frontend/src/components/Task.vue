<template>
  <div class="card">
    <header class="card-header">
      <div class="card-header-title">
        <p>
          <a
            v-if="localTask.issue"
            href="#"
          >
            #{{ localTask.issue }}
          </a> {{ localTask.name }}
        </p>
      </div>
    </header>

    <div class="card-content">
      <p>
        <b-checkbox
          type="is-success"
          @input="updateTask"
          v-model="localTask.done"
        ></b-checkbox> {{ localTask.description }}
      </p>
    </div>

    <footer class="card-footer">
      <a
        @click="editTask"
        class="card-footer-item"
      >
        Editer
      </a>

      <a
        @click="confirmDeleteTask"
        class="card-footer-item"
      >
        Supprimer
      </a>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Task',
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
      this.$store.dispatch('updateTask', this.localTask)
    },
    editTask () {
    },
    confirmDeleteTask () {
      this.$dialog.confirm({
        title: 'Suppression',
        message: 'Êtes-vous certain de vouloir <b>supprimer</b> cette tâche ?',
        confirmText: 'Supprimer',
        cancelText: 'Annuler',
        type: 'is-danger',
        hasIcon: true,
        icon: 'exclamation',
        onConfirm: () => this.deleteTask()
      })
    },
    deleteTask () {
      this.$store.dispatch('deleteTask', this.localTask).then(() => {
        this.$toast.open({
          message: 'Tâche supprimée !',
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
