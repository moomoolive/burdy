import axios from 'axios'
import utils from '../utils/functions.js'

import store from './index.js'

export default {
    mineUrl({ commit }, url) {
        const path = 'http://localhost:5000/review_mine'
        axios.post(path, url, { headers: { Authorization: `Bearer: ${store.state.currentJWT}` } })
          .then((response) => { commit('setData', response.data) })
          .catch((error) => { utils.programError(error, commit) })
    },

    fetchJWT({ commit }, payload) {
        const path = 'http://localhost:5000/login'
        axios.post(path, payload)
          .then((response) => {
            const token = response.data
            localStorage.setItem('token', token)
            axios.defaults.headers.common.Authorization = token
            commit('authorizationSuccess', token)
          })
          .catch((error) => {
            commit('authorizationError', error)
            localStorage.removeItem('token')
          })
    },

    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common.Authorization
        resolve()
      })
    },

    updateUserInfo({ commit }, payload) {
      const path = 'http://localhost:5000/update_info'
      axios.post(path, payload, { headers: { Authorization: `Bearer: ${store.state.currentJWT}` } })
        .then((response) => {
          const updatedToken = response.data
          localStorage.setItem('token', updatedToken)
          commmit('success')
          commit('updateJWT', updatedToken)
          commit('clearError')
        })
        .catch((error) => { utils.programError(error, commit) })
    },

    moveOpinionUnit({ commit }, details) {
      commit('moveReviewMineData', details)
    }
}