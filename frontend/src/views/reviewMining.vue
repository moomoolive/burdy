<template>
  <div class="about">
    <miningUrl
    v-if="showInputForm"
    v-on:url-submitted="onFormSubmission"
    />
    <loadingScreen
    loadingMessage="Please Wait While We Review Mine For You"
    v-if="loading"
    />
    <minedData
    v-if="dataRecieved"
    />
  </div>
</template>

<script>
import miningUrl from '../components/forms/miningUrl.vue'
import loadingScreen from '../components/transitionScreens/loadingScreen.vue'
import minedData from '../components/minedData.vue'

export default {
  name: 'reviewMining',
  components: {
    miningUrl,
    loadingScreen,
    minedData
  },
  data() {
    return {
      showInputForm: true,
      loading: false,
      dataRecieved: false
    }
  },
  methods: {
    onFormSubmission() {
      this.showInputForm = false
      this.loading = true
      this.dataRecieved = false
    }
  },
  computed: {
    reviewMinedData() {
      return this.$store.state.reviewMinedData
    },

    programStatus() {
      return this.$store.state.programStatus.status
    },

    programStatusMessage() {
      return this.$store.state.programStatus.errorMessage
    }
  },
  watch: {
    reviewMinedData(value) {
      if (this.reviewMinedData !== '') {
        this.showInputForm = false
        this.loading = false
        this.dataRecieved = true
      }
    },

    programStatus(value) {
      if (this.programStatus === 'error') {
        this.showInputForm = true
        this.loading = false
        this.dataRecieved = false
        alert(this.programStatusMessage)
      }
    }
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
