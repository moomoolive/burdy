<template>
  <div>
      <div class="confirmationIcon">
        <b-icon icon="check-circle" font-scale="7"></b-icon>
      </div>
      <div class="confirmationMessage">
        <h3>{{ confirmationMessage }}</h3>
      </div>
  </div>
</template>

<script>
export default {
    name: 'confirmationPage',
    props: {
      confirmationMessage: String
    }
}
</script>

<style lang="scss" scoped>
.confirmationIcon {
  margin-top: $topSpacing;
  color: $mainGreen;
}

.confirmationMessage {
  padding-top: $messageSpacing;
}
</style>