import Vue from 'vue'
import VueRouter from 'vue-router'

import home from '../views/home.vue'
import reviewMining from '../views/reviewMining.vue'
import signUp from '../views/signUp.vue'
import profile from '../views/profile.vue'
import login from '../views/login.vue'
import store from '../store/index.js'
import logout from '../views/logout.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/review_mining',
    name: 'reviewMining',
    component: reviewMining,
    meta: {
      requireAuthorization: true
    }
  },
  {
    path: '/sign_up',
    name: 'signUp',
    component: signUp
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: profile,
    meta: {
      requireAuthorization: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/logout/:username',
    name: 'logout',
    component: logout
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireAuthorization)) {
    if (!store.getters.isLoggedIn) {
      next('/login')
      alert('Please login to view this page')
      return
    }
    if (!store.getters.isJWTValid) {
      next('/login')
      alert('Your login has expired. Please sign-in again')
      store.dispatch('logout')
      return
    }
    next()
  } else {
    next()
  }
})

export default router
