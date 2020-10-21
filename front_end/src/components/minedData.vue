<template>
    <div>
        <div>
            <h2 class="head">Classifications</h2>
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
        </div>
        <div>
            <h2 class="head">Move Selected Opinions to Desired Class</h2>
            <div class="buttons">
                <!-- <div class="mt-3">
                    <b-button-group size="large"> -->
                        <b-button pill variant="secondary" v-on:click="movetoClass(0)">Irrelevant</b-button>
                        <b-button pill variant="primary" v-on:click="movetoClass(1)">Use Cases</b-button>
                        <b-button pill variant="success" v-on:click="movetoClass(2)">Benefits</b-button>
                        <b-button pill variant="warning" v-on:click="movetoClass(3)">Complaints</b-button>
                    <!-- </b-button-group>
                </div> -->
            </div>
        </div>
        <div>
            <h2 class="head">Export Selected Opinions to:</h2>
            <div class="buttons">
                <div class="mt-3">
                    <b-button-group size="large">
                        <b-button squared variant="secondary" v-on:click="downloadCSV()">CSV</b-button>
                    </b-button-group>
                </div>
            </div>
        </div>
        <div class='data_container'>
            <h1 class='headers'>
                {{ classNames[shownClass] }}
            </h1>
            <h3 class="headers">
                <small class="instances">{{ classInstances }}</small> instances found
            </h3>
            <b-form-group>
                <b-form-checkbox-group v-model="selected">
                    <div
                    class="sentences"
                    v-for="(opinion, index) in currentlyShownClass"
                    v-bind:key="index"
                    >
                        <b-form-checkbox
                        v-bind:value="shownClass + ':' + index + ':' + opinion"
                        >
                            {{ opinion }}
                        </b-form-checkbox>
                    </div>
                </b-form-checkbox-group>
            </b-form-group>
        </div>
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
            },
            selected: []
        }
    },
    methods: {
        displayClass: function(desiredClass) {
            this.shownClass = desiredClass
        },

        movetoClass(desiredClass) {
            const movementDetails = {
                targetClass: desiredClass,
                info: this.selected
            }
            this.$store.dispatch('moveOpinionUnit', movementDetails)
            this.selected = []
        },

        downloadCSV() {
            const csvEncoding = "data:text/csv;charset=utf-8,"
            const headers = "Classification, Info\n"
            let downloadableContent = csvEncoding + headers
            for (const opinion of this.selected) {
                const key = opinion[0]
                const info = opinion.slice(4)
                const row = `${key},${info.replace(/,/g, "")}\n`
                downloadableContent = downloadableContent.concat(row)
            }
            const encodedrUri = encodeURI(downloadableContent)
            const link = document.createElement("a")
            link.setAttribute('href', encodedrUri)
            link.setAttribute('download', "data.csv")
            document.body.appendChild(link)
            link.click()
            this.selected = []
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

<style lang="scss" scoped>
.buttons {
    margin-bottom: 0.5em;
    margin-top: 0.5em;
}

.data_container {
    border-style: groove;
    text-align: left;
    margin-left: 3em;
    margin-right: 3em;
    /* temporary solution until footer is sticky */
    padding-bottom: 2em;
}

.sentences {
    font-size: medium;
    margin: 0.25em;
}

.headers {
    text-align: center;
    border-bottom: groove;
}

.instances {
    color: red;
}

.head {
    margin-top: 1em;
}
</style>