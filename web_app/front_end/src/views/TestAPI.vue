<template>
    <div>
        <h1>API</h1>
        <h3>{{ ping }}</h3>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'TestAPI',
    data() {
        return {
            ping: ''
        }
    },
    methods: {
        async getPing() {
            const path = 'http://localhost:5000/ping'

            axios.get(path)
                .then((response) => { this.ping = response.data })
                .catch((error) => { console.log(error) })
        }
    },
    created() {
        this.getPing()
    }
}
</script>

<style scoped>

</style>