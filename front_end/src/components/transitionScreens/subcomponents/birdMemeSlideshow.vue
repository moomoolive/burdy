<template>
  <div>
      <div class="general">
            <img v-bind:src="image">
        </div>
  </div>
</template>

<script>
  export default {
    name: 'birdMemeSlideshow',
    data() {
      return {
        imageNum: 0
      }
    },
    created: function() {
        window.setInterval(() => {
            this.changeImage()
            }, 5000)
    },
    methods: {
        changeImage() {
            this.imageNum <= 7 ? this.imageNum++ : this.imageNum = 0
        }
    },
    computed: {
        image() {
            return require(`../../../assets/birdMemes/${this.imageNum}.jpg`)
        }
    }
  }
</script>

<style scoped>
.general {
    margin-top: 2em;
}
</style>