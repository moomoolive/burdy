export default {
    setData: (state, reviewMineData) => {
        state.reviewMinedData = reviewMineData
    },

    authorizationSuccess: (state, token) => {
        state.loginStatus = 'success'
        state.currentJWT = token
    },

    authorizationError: (state) => {
        state.loginStatus = 'error'
    },

    logout: (state) => {
        state.loginStatus = ''
        state.currentJWT = ''
    },

    updateJWT: (state, updatedToken) => {
        state.currentJWT = updatedToken
    },

    moveReviewMineData: (state, movement) => {
        const data = state.reviewMinedData
        const target = data[movement.targetClass]
        for (const opinion of movement.info) {
            const key = opinion[0]
            const index = opinion[2]
            const datapoint = data[key][index]
            delete data[key][index]
            target.push(datapoint)
        }

        for (const key in data) {
            data[key] = data[key].filter((element) => {
                return element !== undefined
            })
        }
    }
}