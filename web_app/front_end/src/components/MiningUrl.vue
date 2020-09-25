<template>
  <div>
    <b-container class="url input form">
      <b-form v-on:submit="onSubmit" v-on:reset="onReset">
        <b-form-group
          id="input-group-1"
          label="Enter your 'Amazon.ca' link here:"
          label-for="input-1"
          description="We'll go the review page and scrapy up any copy-worthy nuggets"
        >
          <b-form-input
            id="input-1"
            v-model="form.url"
            type="url"
            required
            placeholder="amazon.ca/fluffypanda..."
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <ul v-if="showResponses">
        <li v-for="opinion in responseData" v-bind:key="opinion['Opinion Unit']">
          {{ opinion['Opinion Unit'] }} : {{ opinion.Classification }}
        </li>
      </ul>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'miningUrl',
    data() {
      return {
        form: {
          url: ''
        },
        responseData: 'Hello',
        showResponses: null
      }
    },
    methods: {
      initForm() {
        this.form.url = ''
      },

      async mineUrl(payload) {
        const path = 'http://localhost:5000/review_mine'
        await axios.post(path, payload)
          .then((response) => {
            this.responseData = response.data
            this.showResponses = true
          })
          .catch((error) => { console.log(error) })
      },

      onSubmit(event) {
        event.preventDefault()

        const payload = { url: this.form.url }

        this.mineUrl(payload)
        this.initForm()
      },

      onReset(event) {
        event.preventDefault()
        this.form.url = ''
      }
    }
  }

</script>

<style scoped>

</style>