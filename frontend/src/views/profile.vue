<template>
  <div>
    <div class="head">
      <general-form
      formName="updateUserForm"
      loadingMessage="We're updating your information"
      confirmationMessage="Your user information has been updated!"
      redirectLink="/"
      buttonText="To Homepage"
      />
    </div>
  </div>
</template>

<script>
import generalForm from '../components/forms/generalForm.vue'

export default {
    name: 'profile',
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