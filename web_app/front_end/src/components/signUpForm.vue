<template>
  <div>
    <b-container class="url input form">
      <b-form v-on:submit="onSubmit" v-on:reset="onReset" v-on:submit.stop.prevent>
        <b-form-group
          id="input-group-1"
          label="Username: "
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.username"
            v-bind:state="usernameValidation"
            type="text"
            required
            placeholder="the_FLuFfy_panda"
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="usernameValidation">
            Your username must be 1-20 characters long. So choose wisely...
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="usernameValidation">
            Looking Good.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your Email:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.email"
            v-bind:state='emailValidation'
            type="email"
            required
            placeholder="fluffypanda@..."
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="emailValidation">
            Your email cannot be empty or longer than 120 characters.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="emailValidation">
            This should be long enough - just make sure it's an email.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-3" label="Password:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.password"
            v-bind:state="passwordValidation"
            type="password"
            required
            placeholder="Please don't make this 'password'"
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="passwordValidation">
            Your password should be 6-60 characters long.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="passwordValidation">
            You should be good to go.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-4" label="Confirm Password:" label-for="input-4">
          <b-form-input
            id="input-3"
            v-model="form.confirmPassword"
            v-bind:state="passwordValidation"
            type="password"
            required
            placeholder="Please don't make this 'password'"
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="passwordValidation">
            This is not equal to your password.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="passwordValidation">
            There are the same.
          </b-form-valid-feedback>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <h1>{{ form }}</h1>
    </b-container>
  </div>
</template>

<script>
// import axios from 'axios' => to be used in API POST

  export default {
    name: 'signUpForm',
    data() {
      return {
        form: {
          username: '',
          email: '',
          password: '',
          confirmPassword: ''
        }
      }
    },
    methods: {
      initForm() {
        this.form.url = ''
      },

      onSubmit(event) {
        event.preventDefault()

       /* const payload = {
          url: this.form.url
        } */
      this.initForm()
      },

      onReset(evt) {
        evt.preventDefault()
        this.form.username = ''
        this.form.email = ''
        this.form.password = ''
      }
    },
    computed: {
      usernameValidation() {
        return this.form.username.length > 0 && this.form.username.length < 21
      },

      emailValidation() {
        return this.form.email.length > 0 && this.form.email.length < 121
      },

      passwordValidation() {
        return this.form.password.length > 5 && this.form.password.length < 60
      },

      confirmPassword() {
        return this.form.confirmPassword === this.form.password
      }
    }
  }

</script>

<style scoped>

</style>