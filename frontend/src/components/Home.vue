<template>
  <section>
    <Header></Header>
    <Tasks></Tasks>
  </section>
</template>

<script>
import Header from '@/components/Header'
import Tasks from '@/components/Tasks'

export default {
  name: 'Home',
  components: { Header, Tasks }
}
</script>
