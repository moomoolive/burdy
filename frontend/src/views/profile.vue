<template>
  <div>
    <div>
      <div class="head">
        <update-user-form
        v-if="showForm"
        v-on:userInfoUpdated='onFormSubmission'
        />
      </div>
      <loading-screen
      v-if="loading"
      loadingMessage="We're updating your information"
      />
      <confirmation-page
      v-if="confirmation"
      confirmationMessage="Your user information has been updated!"
      redirectLink="/"
      buttonText="To Homepage"
      />
    </div>
  </div>
</template>

<script>
import updateUserForm from '../components/forms/updateUserForm.vue'
import confirmationPage from '../components/transitionScreens/confirmationPage.vue'
import loadingScreen from '../components/transitionScreens/loadingScreen.vue'

export default {
    name: 'profile',
    components: {
      updateUserForm,
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
    },
    methods: {
      onFormSubmission() {
        this.showForm = false
        this.loading = true
    }
  }
}
</script>

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>