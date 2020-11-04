<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
            <b-navbar-brand href="#" v-on:click="clickIcon">
                <i class="fas fa-dove main"></i>
                Burdy
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item>
                    <router-link to="/">Home</router-link>
                </b-nav-item>
                <b-nav-item>
                    <router-link to="/review_mining">Review Mine</router-link>
                </b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template v-slot:button-content>
                    <em class="userInfo">
                        <small v-if="isLoggedIn">Welcome, {{username}}</small>
                        <small v-else>User</small>
                    </em>
                </template>
                    <div>
                        <div v-if="isLoggedIn">
                            <b-dropdown-item>
                                <router-link v-bind:to="'/profile/' + username">
                                    Profile Settings
                                </router-link>
                            </b-dropdown-item>
                            <b-dropdown-item>
                                <router-link v-bind:to="'/logout/' + username">
                                    Logout
                                </router-link>
                            </b-dropdown-item>
                        </div>
                            <div v-if="!isLoggedIn">
                            <b-dropdown-item>
                                <router-link to="/sign_up">Sign Up</router-link>
                            </b-dropdown-item>
                            <b-dropdown-item>
                                <router-link to="/login">Login</router-link>
                            </b-dropdown-item>
                        </div>
                    </div>
                </b-nav-item-dropdown>
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
export default {
    name: 'Header',
    computed: {
        isLoggedIn() { return this.$store.getters.isLoggedIn },

        username() {
            return this.$store.getters.userInfo.username
            }
    },
    methods: {
        clickIcon() {
            this.$router.push('/')
        }
    }
}
</script>

<style lang="scss" scoped>
.main {
    color: $primaryColor;
}

.userInfo {
    color: white;
    margin-top: 0.5em;
}

</style>