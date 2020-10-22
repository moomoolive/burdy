<template>
    <div>
        <confirmation-page
        confirmationMessage="You've Been Logged Out. We're Redirecting You..."
        redirectLink="/"
        />
    </div>
</template>

<script>
import confirmationPage from '../components/transitionScreens/confirmationPage.vue'
import sleep from '../utils/functions.js'

export default {
    name: 'logout',
    components: {
        confirmationPage
    },
    mounted() {
        this.$nextTick(async function() {
            this.$store.dispatch('logout')
            await sleep(3000)
            .then(() => {
                this.$router.push('/login/')
            })
        })
    }
}
</script>

<style lang="scss" scoped>

</style>