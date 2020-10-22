<template>
  <div>
    <div class="head">
      <h1>Sign Up</h1>
      <signUpForm />
    </div>
  </div>
</template>

<script>
import signUpForm from '../components/forms/signUpForm.vue'

export default {
  name: 'signUp',
  components: {
    signUpForm
  }
}
</script>

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>