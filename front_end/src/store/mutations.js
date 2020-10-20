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
        const target = state.reviewMinedData[movement.targetClass]
        for (let i = 0; i < movement.info.length; i++) {
            const opinion = movement.info[i]
            const classNumber = opinion[0]
            const orderNumber = opinion[2]
            const datacopy = state.reviewMineData[classNumber][orderNumber]
            delete state.reviewMineData[classNumber][orderNumber]
            target.push(datacopy)
        }
        for (const classification in state.reviewMineData) {
            for (const opinion in classification) {
                if (opinion === undefined) {
                    const deleter = classification.splice(i, i + 1)
                }
            }
        }
    }
}