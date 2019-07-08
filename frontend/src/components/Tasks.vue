<template>
  <section class="section">
    <div class="columns">
      <div class="column is-three-fifths is-offset-one-fifth">
      </div>
    </div>
  </section>
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
