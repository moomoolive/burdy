import Vue from 'vue'
import VueRouter from 'vue-router'

import home from '../views/home.vue'
import reviewMining from '../views/reviewMining.vue'
import signUp from '../views/signUp.vue'
import profile from '../views/profile.vue'
import login from '../views/login.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/review_mining',
    name: 'reviewMining',
    component: reviewMining
  },
  {
    path: '/sign_up',
    name: 'signUp',
    component: signUp
  },
  {
    path: '/profile',
    name: 'profile',
    component: profile
  },
  {
    path: '/login',
    name: 'login',
    component: login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
