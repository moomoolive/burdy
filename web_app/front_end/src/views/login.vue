<template>
  <div class="home">
    <h1>Login</h1>
    <loginForm />
  </div>
</template>

<script>
import loginForm from '../components/forms/loginForm.vue'

export default {
  name: 'login',
  components: {
    loginForm
  }
}
</script>

<style scoped>

</style>