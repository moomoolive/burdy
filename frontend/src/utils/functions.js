import axios from 'axios'

const functions = {
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms))
    },
    async updateProgramStatus(statusCode, message = '', commit) {
        const data = {
            status: statusCode,
            message: message
        }
        commit('updateProgramStatus', data)
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
    },
    usernameRequirements(username) {
        const condition1 = username.length > 0
        const condition2 = username.length < 21

        return condition1 && condition2
    },
    emailRequirements(email) {
        const condition1 = email.length > 0
        const condition2 = email.length < 121

        return condition1 && condition2
    }
}

export default functions