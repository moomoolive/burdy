<template>
  <div>
    <div class="general">
      <h1>Profile Settings</h1>
      <div class="settings">
        <p> Username: {{ userInfo.username }} </p>
        <p> Email: {{ userInfo.email }} </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'profile',
  components: {},
  computed: {
    userInfo() {
      return this.$store.getters.userInfo
    }
  }
}
</script>

<style scoped>
.general {
  margin-top: 3em;
}

.settings {
  margin-top: 2em;
}
</style>