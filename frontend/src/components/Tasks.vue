<template>
  <p>
    Tasks
  </p>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Tasks',
  computed: {
    ...mapState([ 'tasks' ])
  },
  created () {
    if (!this.tasks.length) this.$store.dispatch('getTasks')
  }
}
</script>
