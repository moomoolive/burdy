<template>
    <div>
        <div class='footerSpacing'>
            <b-navbar variant="dark" type="dark" fixed="bottom">
                <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="I want to find..."></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>
                <b-nav-text class="ml-auto">
                    <small class="copyright">
                        All Rights Reserved. Burdy ©
                    </small>
                </b-nav-text>
            </b-navbar>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style lang="scss" scoped>
.copyright {
    font-size: x-small;
    color: $layoutSecondary;
}
</style>