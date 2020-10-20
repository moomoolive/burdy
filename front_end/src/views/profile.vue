<template>
  <div>
    <div>
      <div class="head">
        <update-user-form
        v-if="showForm"
        v-on:userInfoUpdated='onFormSubmission'
        />
      </div>
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

export default {
    name: 'profile',
    components: {
      updateUserForm,
      confirmationPage
    },
    data() {
      return {
        showForm: true,
        confirmation: false
      }
    },
    methods: {
      onFormSubmission() {
        this.showForm = false
        this.confirmation = true
      }
    }
  }

</script>

<style lang="scss" scoped>
.head {
  margin-top: $topForm;
}
</style>