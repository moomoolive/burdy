<template>
  <div>
    <div class="head">
      <h1>Login</h1>
      <loginForm />
    </div>
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

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>