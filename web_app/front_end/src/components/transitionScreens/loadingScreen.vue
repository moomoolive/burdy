<template>
    <div class="loadingGeneral">
        <b-overlay v-bind:show='true' rounded="lg" opacity="0.6">
            <template v-slot:overlay>
                <div class="d-flex align-items-center">
                <b-spinner small type="grow" variant="secondary"></b-spinner>
                <b-spinner type="grow" variant="dark"></b-spinner>
                <b-spinner small type="grow" variant="secondary"></b-spinner>
                <!-- We add an SR only text for screen readers -->
                <span class="sr-only">Please wait...</span>
                </div>
            </template>
        </b-overlay>
        <div class="loadingMessage">
            <h3>{{ loadingMessage }}</h3>
        </div>
        <div>
            <birdMemeSlideshow />
        </div>
    </div>
</template>

<script>
import birdMemeSlideshow from '../subcomponents/birdMemeSlideshow.vue'

export default {
    name: 'loadingScreen',
    props: {
        loadingMessage: String
    },
    components: {
        birdMemeSlideshow
    }
}
</script>

<style lang="scss" scoped>
.loadingGeneral {
    margin-top: $topSpacing;
}

.loadingMessage {
    padding-top: $messageSpacing;
}
</style>