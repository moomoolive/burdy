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
            <div class='data_container'>
                <h1 class='headers'>
                    {{ classNames[shownClass] }}
                </h1>
                <h3 class="headers">
                    {{ classInstances }} instances found
                </h3>
                    <p
                    class="sentences"
                    v-for="opinion in currentlyShownClass"
                    v-bind:key="opinion"
                    >
                        {{ opinion }}
                    </p>
            </div>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'minedData',
    data() {
        return {
            shownClass: 1,
            classNames: {
                0: 'Irrelevant',
                1: 'Use Cases',
                2: 'Benefits',
                3: 'Complaints'
            }
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
        },
        classInstances() {
            return this.currentlyShownClass.length
        }
    }
}
</script>

<style scoped>
.buttons {
    margin-bottom: 2em;
    margin-top: 2em;
}

.data_container {
    border-style: groove;
    text-align: left;
    margin-left: 3em;
    margin-right: 3em;
}

.sentences {
    font-size: medium;
    margin: 0.25em;
}

.headers {
    text-align: center;
    border-bottom: groove;
}
</style>