import axios from 'axios'

export default {
    async mineUrl({ commit }, url) {
        const path = 'http://localhost:5000/review_mine'
        await axios.post(path, url)
          .then((response) => {commit('setData', response.data)})
          .catch((error) => {console.log('Failed to fetch Url', error)})
    },
    async fetchJWT({ commit }, payload) {
      const path = 'http://localhost:5000/authenticate'
      await axios.post(path, payload)
        .then((response) => {commit('setJWT', response.data)})
        .catch((error) => {console.log('Error Authenticating', error)})
    }
}