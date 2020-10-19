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
    }
}