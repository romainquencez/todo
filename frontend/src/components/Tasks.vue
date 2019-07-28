<template>
  <section class="section">
    <div class="columns">
      <div class="column">
        <b-button
          @click="createTask"
          type="is-success"
          icon-left="plus"
        >
          Créer une nouvelle tâche
        </b-button>
      </div>
    </div>

    <div class="columns">
      <div class="column is-three-fifths is-offset-one-fifth">
        <task
          v-for="task in tasks"
          :key="task.id"
          :task="task"
        />
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex'
import Task from '@/components/Task'
import UpdateOrCreateTaskModal from '@/components/UpdateOrCreateTaskModal'

export default {
  name: 'Tasks',
  components: {
    Task
  },
  computed: {
    ...mapState([ 'tasks' ])
  },
  created () {
    if (!this.tasks.length) this.$store.dispatch('getTasks')
  },
  methods: {
    createTask () {
      this.$modal.open({
        parent: this,
        component: UpdateOrCreateTaskModal,
        props: {
          task: {}
        },
        hasModalCard: true
      })
    }
  }
}
</script>
