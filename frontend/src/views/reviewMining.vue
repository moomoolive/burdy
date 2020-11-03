<template>
  <div class="about">
    <general-form
    formName="miningUrl"
    loadingMessage="Please Wait While We Review Mine For You"
    confirmation="minedData"
    />
  </div>
</template>

<script>
import generalForm from '../components/forms/generalForm.vue'

export default {
  name: 'reviewMining',
  components: {
    generalForm
  },
  beforeRouteLeave (to, from, next) {
    const answer = window.confirm('Do you really want to leave? Any data on this page will be erased!')
    if (answer) {
        next()
    } else {
        next(false)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
