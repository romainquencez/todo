<template>
  <div class="card">
    <header class="card-header">
      <div class="card-header-title">
        <p>
          <a
            v-if="localTask.issue"
            :href="issueUrl"
            target="_blank"
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
        <span class="icon">
          <font-awesome-icon icon="edit"></font-awesome-icon>
        </span>
        Editer
      </a>

      <a
        @click="confirmDeleteTask"
        class="card-footer-item has-text-danger"
      >
        <span class="icon">
          <font-awesome-icon icon="trash"></font-awesome-icon>
        </span>
        Supprimer
      </a>
    </footer>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import UpdateOrCreateTaskModal from '@/components/UpdateOrCreateTaskModal'

export default {
  name: 'Task',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  computed: {
    ...mapState([ 'me' ]),
    localTask () {
      return { ...this.task }
    },
    issueUrl () {
      if (
        this.me.api_url &&
        this.localTask.issue
      ) {
        return `${this.me.api_url}issues/${this.localTask.issue}`
      }
      return String
    }
  },
  methods: {
    updateTask () {
      this.$store.dispatch('updateTask', this.localTask)
    },
    editTask () {
      this.$modal.open({
        parent: this,
        component: UpdateOrCreateTaskModal,
        props: {
          task: this.localTask
        },
        hasModalCard: true
      })
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
