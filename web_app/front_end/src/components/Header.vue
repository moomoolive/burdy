<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
            <b-navbar-brand href="http://localhost:8080/">
                <i class="fas fa-dove main"></i>
                Burdy
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item href="#">
                    <router-link to="/">Home</router-link>
                </b-nav-item>
                <b-nav-item href="#">
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
                                <router-link to="/profile">Profile Settings</router-link>
                            </b-dropdown-item>
                            <b-dropdown-item
                            v-on:click='logout'
                            >
                                Sign Out
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
    methods: {
        logout: function() {
            this.$store.dispatch('logout')
                .then(() => {
                    this.$router.push('/login')
                })
        }
    },
    computed: {
        isLoggedIn() { return this.$store.getters.isLoggedIn },

        username() {
            return this.$store.getters.userInfo.username
            }
    }
}
</script>

<style scoped>
.main {
    color: #42b983 !important;
}

.userInfo {
    color: white;
    margin-top: 0.5em;
}

</style>