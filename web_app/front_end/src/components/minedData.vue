<template>
    <div>
        <ul>
            <li v-for="opinion in reviewMinedData" v-bind:key="opinion['Opinion Unit']">
                {{ opinion['Opinion Unit'] }} : {{ opinion.Classification }}
            </li>
      </ul>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'minedData',
    computed: mapState(['reviewMinedData'])
}
</script>

<style scoped>

</style>