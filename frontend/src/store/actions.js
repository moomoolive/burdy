import axios from 'axios'
import utils from '../utils/functions.js'

import store from './index.js'

export default {
    mineUrl({ commit }, url) {
        const path = 'http://localhost:5000/review_mine'
        axios.post(path, url, { headers: { Authorization: `Bearer: ${store.state.currentJWT}` } })
          .then((response) => { commit('setData', response.data) })
          .catch((error) => { utils.updateProgramStatus('error', error, commit) })
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
          utils.updateProgramStatus('success', response.data, commit)
          commit('updateJWT', updatedToken)
        })
        .catch((error) => { utils.updateProgramStatus('error', error, commit) })
    },
    moveOpinionUnit({ commit }, details) {
      commit('moveReviewMineData', details)
    },
    signUpUser({ commit }, payload) {
      const path = 'http://localhost:5000/sign_up'
      axios.post(path, payload)
        .then((response) => { utils.updateProgramStatus('success', response.data, commit) })
        .catch((error) => { utils.updateProgramStatus('error', error, commit) })
    },
    formSubmisson({ commit }) {
      commit('formSubmitted')
    }
}