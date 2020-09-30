import axios from 'axios'

import store from './index.js'

export default {
    async mineUrl({ commit }, url) {
        const path = 'http://localhost:5000/review_mine'
        await axios.post(path, url, { headers: { Authorization: `Bearer: ${store.state.currentJWT}` } })
          .then((response) => { commit('setData', response.data) })
          .catch((error) => { console.log('Failed to fetch Url', error) })
    },

    fetchJWT({ commit }, payload) {
      return new Promise((resolve, reject) => {
        const path = 'http://localhost:5000/login'
        axios.post(path, payload)
          .then((response) => {
            const token = response.data
            localStorage.setItem('token', token)
            axios.defaults.headers.common.Authorization = token
            commit('authorizationSuccess', token)
            resolve(response)
      })
        .catch((error) => {
          commit('authorizationError', error)
          localStorage.removeItem('token')
          reject(error)
        })
      })
    },

    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common.Authorization
        resolve()
      })
    }
}