<template>
  <div>
    <div class="head">
      <h1>Sign Up</h1>
      <signUpForm
      v-if="showForm"
      />
      <confirmation-page
      v-if="confirmation"
      confirmationMessage="You've been successfully signed up!"
      redirectLink='/login'
      buttonText="Start Using Burdy Now!"
      />
      <loading-screen
      v-if="loading"
      loadingMessage="We're signing you up. Just a moment."
      />
    </div>
  </div>
</template>

<script>
import signUpForm from '../components/forms/signUpForm.vue'
import confirmationPage from '../components/transitionScreens/confirmationPage.vue'
import loadingScreen from '../components/transitionScreens/loadingScreen.vue'

export default {
  name: 'signUp',
  components: {
    signUpForm,
    confirmationPage,
    loadingScreen
  },
  data() {
    return {
      showForm: true,
      loading: false,
      confirmation: false
    }
  },
  computed: {
    programStatusMessage() {
        return this.$store.state.programStatus.errorMessage
      },

      programStatus() {
        return this.$store.state.programStatus.status
      }
  },
  watch: {
    programStatus(value) {
        this.loading = false
        if (this.programStatus === 'success') {
          this.confirmation = true
        }
        if (this.programStatus === 'error') {
          this.showForm = true
          alert(this.programStatusMessage)
        }
      }
  }
}
</script>

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>