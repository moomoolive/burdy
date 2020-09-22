import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import ReviewMining from '../views/ReviewMining.vue'
import TestAPI from '../views/TestAPI.vue'

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
    path: '/test_api',
    name: 'TestAPI',
    component: TestAPI
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
