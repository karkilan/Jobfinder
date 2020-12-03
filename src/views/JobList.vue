<template>
  <div class="jobs">
    <Create />
  </div>
</template>

<script>
// @ is an alias to /src
import Create from '@/components/Create.vue'

export default {
  name: 'JobList',
  components: {
    Create
  }
}
</script>