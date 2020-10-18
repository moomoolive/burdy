<template>
  <div class="inputGeneral">
    <h1> Update Profile </h1>
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
            placeholder="da_FLuFfy_burdy"
            v-on:input="username => checkUniqueness('username', username, 'uniqueUsername')"
          />
          <b-form-invalid-feedback v-bind:state="usernameValidation">
            <div v-if="!uniqueUsername">
              You need an original username. Be a little creative. We believe in you.
            </div>
            <div v-if="form.username.length > 20">
              Your username is too long.
            </div>
            <div v-if="form.username.length < 1">
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
            placeholder="beautifulburdy@burdyparadise.com"
            v-on:input="email => checkUniqueness('email', this.form.email, 'uniqueEmail')"
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="emailValidation">
            <div v-if="form.email.length > 120">
              Your email can't be longer than 120 characters.
            </div>
            <div v-if="form.email.length < 1">
              C'mon, you must have an email.
            </div>
            <div v-if="!uniqueEmail">
              Looks like this email is already in our database. Second account?
            </div>
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind="emailValidation">
            Yep! That looks like an email.
          </b-form-valid-feedback>
        </b-form-group>

        <b-button type="submit" variant="success">Confirm Changes</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../store/index.js'

  export default {
    name: 'profile',
    data() {
      return {
        form: {
          username: '',
          email: ''
        },
        uniqueUsername: true,
        uniqueEmail: true
      }
    },
    methods: {
      initForm() {
        this.form.username = this.userInfo.username
        this.form.email = this.userInfo.email
      },

      onSubmit(event) {
        event.preventDefault()

        const payload = {
          originalUsername: this.userInfo.username,
          username: this.form.username,
          email: this.form.email
        }

        this.$store.dispatch('updateUserInfo', payload)
        this.initForm()
      },

      onReset(event) {
        event.preventDefault()

        this.initForm()
      },

      async checkUniqueness(dataType, toBeChecked, value) {
        const path = 'http://localhost:5000/check_unique'
        const payload = {
          type: dataType,
          data: toBeChecked
        }
        const response = await axios.post(path, payload)
        this[value] = response.data === 'unique'

        return this[value]
      }
    },
    computed: {
      usernameValidation() {
        const condition1 = this.form.username.length > 0
        const condition2 = this.form.username.length < 21
        const condition3 = this.uniqueUsername

        return condition1 && condition2 && condition3
      },

      emailValidation() {
        const condition1 = this.form.email.length > 0
        const condition2 = this.form.email.length < 121
        const condition3 = this.uniqueEmail

        return condition1 && condition2 && condition3
      },

      userInfo() {
        return this.$store.getters.userInfo
      }
    },
    created() {
      this.initForm()
    }
  }

</script>

<style scoped>
.inputGeneral {
  margin-top: 5em;
}
</style>