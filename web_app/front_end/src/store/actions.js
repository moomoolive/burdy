import axios from 'axios'

export default {
    async mineUrl({ commit }, url) {
        const path = 'http://localhost:5000/review_mine'
        const response = await axios.post(path, url)

        commit('setData', response.data)
      }
}