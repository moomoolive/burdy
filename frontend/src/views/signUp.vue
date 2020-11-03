<template>
  <div>
    <div class="head">
      <h1>Sign Up</h1>
      <general-form
      formName="signUpForm"
      loadingMessage="We're signing you up. Just a moment."
      confirmationMessage="You've been successfully signed up!"
      redirectLink="/login"
      buttonText="Start Using Burdy Now!"
      />
    </div>
  </div>
</template>

<script>
import generalForm from '../components/forms/generalForm.vue'

export default {
  name: 'signUp',
  components: {
    generalForm
  }
}
</script>

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>