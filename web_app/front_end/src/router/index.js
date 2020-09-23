import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import ReviewMining from '../views/ReviewMining.vue'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
