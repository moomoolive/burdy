import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import ReviewMining from '../views/ReviewMining.vue'
import login from '../views/login.vue'
import Profile from '../views/Profile.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/review_mining',
    name: 'ReviewMining',
    component: ReviewMining
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
