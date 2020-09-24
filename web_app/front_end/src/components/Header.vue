<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="dark">
            <b-navbar-brand href="#">
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
                        <b-dropdown-item href="#">
                            <router-link to="/profile">Profile</router-link>
                        </b-dropdown-item>
                        <b-dropdown-item href="#">
                            Sign Out
                        </b-dropdown-item>
                        <b-dropdown-item href="#">
                            <router-link to="/sign_up">Sign Up</router-link>
                        </b-dropdown-item>
                        <b-dropdown-item href="#">
                            <router-link to="/login">Login</router-link>
                        </b-dropdown-item>
                    </div>
                </b-nav-item-dropdown>
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>

<style scoped>
.main {
    color: #42b983;
}

</style>