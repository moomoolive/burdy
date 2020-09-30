<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark">
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
                <b-nav-form>
                    <b-form-input size="sm" class="mr-sm-2" placeholder="I want to find..."></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>

                <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
                <template v-slot:button-content>
                    <em>User</em>
                </template>
                    <div>
                        <div v-if="isLoggedIn">
                            <b-dropdown-item>
                                <router-link to="/profile">Profile</router-link>
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
    computed: {
        isLoggedIn: function() { return this.$store.getters.isLoggedIn }
    },
    methods: {
        logout: function() {
            this.$store.dispatch('logout')
                .then(() => {
                    this.$router.push('/login')
                })
        }
    }
}
</script>

<style scoped>
.main {
    color: #42b983;
}

</style>