<template>
  <div id="app">
    <div id="nav">
      <Header />
      <div class="footer">
        <Footer />
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/layout/Header.vue'
import Footer from './components//layout/Footer.vue'

export default {
  components: {
    Header,
    Footer
  },
  created: function() {
    if (this.$store.getters.isJWTExpired) {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $layoutPrimary;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: $layoutSecondary;

    &.router-link-exact-active {
      color: $primaryColor;
    }
  }
}
</style>
