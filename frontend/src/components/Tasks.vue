<template>
  <section class="section">
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
  }
}
</script>
