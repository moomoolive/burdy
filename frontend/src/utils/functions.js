import axios from 'axios'

const functions = {

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms))
    },

    async updateProgramStatus(message = '', commit, statusCode) {
        commit('updateProgramStatus', message, statusCode)
            await this.sleep(3000)
            .then(() => {
                commit('clearProgramStatus')
            })
    },

    randomNumber(maxRange) {
        return Math.floor(Math.random() * maxRange)
    },

    async checkUniqueness(dataType, toBeChecked, value) {
        const path = 'http://localhost:5000/check_unique'
        const payload = {
          type: dataType,
          data: toBeChecked
        }
        const response = await axios.post(path, payload)
        this[value] = response.data === 'unique'

        return this[value]
      }
}

export default functions