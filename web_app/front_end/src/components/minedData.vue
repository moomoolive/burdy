<template>
    <div>
        <div class="buttons">
            <div class="mt-3">
                <b-button-group size="large">
                    <b-button variant="secondary" v-on:click="displayClass(0)">Irrelevant</b-button>
                    <b-button variant="primary" v-on:click="displayClass(1)">Use Cases</b-button>
                    <b-button variant="success" v-on:click="displayClass(2)">Benefits</b-button>
                    <b-button variant="warning" v-on:click="displayClass(3)">Complaints</b-button>
                </b-button-group>
            </div>
        </div>
        <ul>
            <li v-for="opinion in currentlyShownClass" v-bind:key="opinion">
                {{ opinion }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'minedData',
    data() {
        return {
            shownClass: 1
        }
    },
    methods: {
        displayClass: function(desiredClass) {
            this.shownClass = desiredClass
        }
    },
    computed: {
        reviewMinedData() {
            return this.$store.state.reviewMinedData
        },
        currentlyShownClass() {
            return this.reviewMinedData[this.shownClass]
        }
    }
}
</script>

<style scoped>
.buttons {
    margin-bottom: 1em;
}
</style>