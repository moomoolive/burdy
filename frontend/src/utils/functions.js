const functions = {

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms))
    },

    async programError(error, commit) {
        commit('errorStatus', error)
            await this.sleep(3000)
            .then(() => {
                commit('clearError')
            })
    },

    randomNum(maxRange) {
        return Math.floor(Math.random() * maxRange)
    }
}

export default functions