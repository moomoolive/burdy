<template>
  <div class="inputGeneral">
    <b-container class="signup form">
      <b-form v-on:submit="onSubmit" v-on:reset="onReset">
        <b-form-group
          id="input-group-1"
          label="Username: "
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="username"
            type="text"
            required
            placeholder="da_FLuFfy_burdy"
          />
        </b-form-group>

        <b-form-group id="input-group-3" label="Password:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="password"
            type="password"
            required
            placeholder="********"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="success">Login</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'loginForm',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    initForm() {
      this.username = ''
      this.password = ''
    },
    onSubmit(event) {
      event.preventDefault()
      const payload = {
          username: this.username,
          password: this.password
      }
      this.$store.dispatch('formSubmisson')
      this.$store.dispatch('fetchJWT', payload)
      this.initForm()
    },
    onReset(event) {
      event.preventDefault()
      this.initForm()
    }
  },
  watch: {
    login() {
      if (this.login === 'success') this.$router.push('/')
    }
  },
  computed: {
    login() {
      return this.$store.state.loginStatus
    }
  }
}
</script>

<style lang="scss" scoped>
.inputGeneral {
  margin-top: $headInputSpace;
}

</style>