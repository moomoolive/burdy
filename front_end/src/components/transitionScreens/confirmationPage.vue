<template>
  <div>
      <div class="confirmationIcon">
        <b-icon icon="check-circle" font-scale="7"></b-icon>
      </div>
      <div class="confirmationMessage">
        <h3>{{ confirmationMessage }}</h3>
      </div>
      <div v-if="!!buttonText">
        <b-button class="redirectButton">
          <router-link v-bind:to="redirectLink">
            <div class="linkText">{{ buttonText }}</div>
          </router-link>
        </b-button>
      </div>
  </div>
</template>

<script>
export default {
    name: 'confirmationPage',
    props: {
      confirmationMessage: String,
      redirectLink: String,
      buttonText: {
        type: String,
        required: false
        }
    }
}
</script>

<style lang="scss" scoped>
.confirmationIcon {
  margin-top: $topSpacing;
  color: $primaryColor;
}

.confirmationMessage {
  padding-top: $messageSpacing;
  padding-bottom: $messageSpacing;
}

.redirectButton {
  border-color: $primaryColor !important;
  background-color: $secondaryColor !important;
}

.linkText {
  color: $primaryColor;
  font-weight: bold;
}
</style>