<template>
  <div>
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
    <ul>
      <li v-for="opinion in form.responseData" v-bind:key="opinion['Opinion Unit']">
        {{ opinion['Opinion Unit'] }} : {{ opinion.Classification }}
      </li>
    </ul>
    <h1>{{ form.responseData }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
        form: {
          url: '',
          responseData: 'Hello'
        }
      }
    },
    methods: {
      initForm() {
        this.form.url = ''
      },

      async classifiyOpinionUnits(opinionUnits) {
        const path = 'http://localhost:5000/review_mine'
        const response = await axios.post(path, opinionUnits)
          .then((response) => { this.form.responseData = response.data })
          .catch((error) => { console.log(error) })

        return response
      },

      async retrieveOpinionUnits(payload) {
        const path = `http://localhost:9080/crawl.json?spider_name=burdy_scraper&url=${payload.url}`
        const response = await axios.get(path)
          .then((response) => {
            this.form.responseData = response.data.items
          })
          .catch((error) => { console.log(error) })

        this.classifiyOpinionUnits(this.form.responseData)

        return response
      },

      onSubmit(event) {
        event.preventDefault()

        const payload = {
          url: this.form.url
        }
      this.initForm()
      this.retrieveOpinionUnits(payload)
      },

      onReset(evt) {
        evt.preventDefault()
        this.form.url = ''
      }
    }
  }

</script>

<style scoped>

</style>