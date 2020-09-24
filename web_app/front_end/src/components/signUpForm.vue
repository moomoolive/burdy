<template>
  <div>
    <b-container class="signup form">
      <b-form v-on:submit="onSubmit" v-on:reset="onReset">
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
            <div v-if="!unique">
              You need an original username. Be a little creative. We believe in you.
            </div>
            <div v-else-if="form.username.length > 20">
              Your username is too long.
            </div>
            <div v-else-if="form.username.length < 1">
              You can't have a blank username.
            </div>
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
            <div v-if="form.email.length > 120">
              Your email can't be longer than 120 characters.
            </div>
            <div v-else-if="form.email.length < 1">
              C'mon, you must have an email.
            </div>
            <div v-else-if="!uniqueEmail">
              Looks like this email is already in our database. Second account?
            </div>
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="emailValidation">
            Yep! That looks like an email.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-3" label="Password:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="form.password"
            v-bind:state="passwordValidation"
            type="password"
            required
            placeholder="Please, please, don't make this 'password'. Please."
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="passwordValidation">
            Your password must be 6-60 characters long.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="passwordValidation">
            You should be good to go.
          </b-form-valid-feedback>
        </b-form-group>

        <b-form-group id="input-group-4" label="Confirm Password:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="form.confirmPassword"
            v-bind:state="confirmPassword"
            type="password"
            required
            placeholder="Don't mess up. No pressure!"
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="confirmPassword">
            This is not equal to your password.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="confirmPassword">
            They are the same.
          </b-form-valid-feedback>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'signUpForm',
    data() {
      return {
        form: {
          username: '',
          email: '',
          password: '',
          confirmPassword: ''
        },
        uniqueUsername: false,
        uniqueEmail: false
      }
    },
    methods: {
      initForm() {
        this.form.username = ''
        this.form.email = ''
        this.form.password = ''
        this.form.confirmPassword = ''
      },

      async signUpUser(payload) {
        const path = 'http://localhost:5000/sign_up'
        const response = await axios.post(path, payload)
          .then((response) => { console.log(response) })
          .catch((error) => { console.log(error) })

        return response
      },

      onSubmit(event) {
        event.preventDefault()

        const payload = this.form

        this.signUpUser(payload)
        this.initForm()
      },

      onReset(event) {
        event.preventDefault()

        this.form.username = ''
        this.form.email = ''
        this.form.password = ''
        this.form.confirmPassword = ''
      },

      async checkUniqueness(dataType, toBeChecked, value) {
        const path = 'http://localhost:5000/check_unique'
        const payload = {
          type: dataType,
          data: toBeChecked
        }
        await axios.post(path, payload)
          .then((response) => (
            this.unique = response.data === 'true'
          ))
          .catch((error) => (console.log(error)))
      }
    },
    computed: {
      usernameValidation() {
        this.checkUniqueness('username', this.form.username, this.uniqueUsername)
        const condition1 = this.form.username.length > 0
        const condition2 = this.form.username.length < 21
        const condition3 = this.unique

        return condition1 && condition2 && condition3
      },

      emailValidation() {
        this.checkUniqueness('email', this.form.email, this.uniqueEmail)
        const condition1 = this.form.email.length > 0
        const condition2 = this.form.email.length < 121
        const condition3 = this.uniqueEmail

        return condition1 && condition2 && condition3
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