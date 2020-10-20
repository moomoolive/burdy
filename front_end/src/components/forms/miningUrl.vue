<template>
  <div class="inputGeneral">
    <b-container class="url input form">
      <b-form v-on:submit="onSubmit" v-on:reset="onReset">
        <h3 class="inputHeading">Enter your 'Amazon.ca' link here:</h3>
        <b-form-group
          id="input-group-1"
          label-for="input-1"
          description="We'll go the review page and scrapy up any copy-worthy nuggets"
        >
          <b-form-input
            id="input-1"
            v-model="form.url"
            v-bind:state="amazonCaValidation"
            type="url"
            required
            placeholder="amazon.ca/fluffycoolburdy..."
          ></b-form-input>
          <b-form-invalid-feedback v-bind:state="amazonCaValidation">
            We can only mine Amazon Canada reviews.
          </b-form-invalid-feedback>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'miningUrl',
    data() {
      return {
        form: {
          url: ''
        }
      }
    },
    methods: {
      ...mapActions(['mineUrl']),
      initForm() {
        this.form.url = ''
      },

      onSubmit(event) {
        event.preventDefault()
        this.$emit('url-submitted')

        const payload = { url: this.form.url }

        this.mineUrl(payload)
        this.initForm()
      },

      onReset(event) {
        event.preventDefault()
        this.form.url = ''
      }
    },
    computed: {
      amazonCaValidation() {
        return this.form.url.search('amazon.ca') !== -1
      }
    }
  }

</script>

<style lang="scss" scoped>
.inputGeneral {
    margin-top: 14em;
}

.inputHeading {
  margin-bottom: 1.5em;
  font-weight: bold;
}
</style>