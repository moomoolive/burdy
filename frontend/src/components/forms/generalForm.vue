<template>
    <div>
        <component
        :is="formName"
        v-if="showForm"
        ></component>
        <loadingScreen
        v-if="loading"
        :loadingMessage="loadingMessage"
        />
        <component
        v-bind:is="confirmation"
        v-if="final"
        :confirmationMessage="confirmationMessage"
        :redirectLink="redirectLink"
        :buttonText="buttonText"
        ></component>
    </div>
</template>

<script>
import loginForm from './input/loginForm'
import miningUrl from './input/miningUrl'
import signUpForm from './input/signUpForm'
import updateUserForm from './input/updateUserForm'

import loadingScreen from '../transitionScreens/loadingScreen.vue'

import confirmationPage from '../transitionScreens/confirmationPage.vue'
import minedData from '../minedData.vue'

export default {
    name: 'generalForm',
    components: {
        loadingScreen,
        confirmationPage,
        minedData,
        loginForm,
        miningUrl,
        signUpForm,
        updateUserForm
    },
    props: {
        formName: String,
        confirmation: {
            type: String,
            default: 'confirmationPage',
            required: false
        },
        loadingMessage: String,
        // only props below when confirmationPage component is used
        confirmationMessage: {
            type: String,
            required: false
            },
        redirectLink: {
            type: String,
            required: false
            },
        buttonText: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            showForm: true,
            loading: false,
            final: false
        }
    },
    computed: {
        programStatus() {
            return this.$store.state.programStatus.status
        },

        programStatusMessage() {
            return this.$store.state.programStatus.errorMessage
        }
    },
    watch: {
        programStatus(value) {
        this.loading = false
        if (this.programStatus === 'form submitted') {
            this.showForm = false
            this.loading = true
        }
        if (this.programStatus === 'success') {
          this.final = true
        }
        if (this.programStatus === 'error') {
          this.showForm = true
          alert(this.programStatusMessage)
        }
      }
    }
}
</script>

<style>

</style>