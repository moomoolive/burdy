import state from './state.js'

export default {
    isLoggedIn: (state) => (!!state.currentJWT),

    decodedJWT: (state) => {
        const token = state.currentJWT
        const tokenInfoSection = token.split('.')[1]
        const decodedTokenInfo = atob(tokenInfoSection)
        const jsonTokenInfo = JSON.parse(decodedTokenInfo)

        return jsonTokenInfo
    },

    userInfo: (state, getters) => (
        {
            username: getters.decodedJWT.user,
            email: getters.decodedJWT.email
        }
        ),

    isJWTValid: (state, getters) => {
        const tokenInfo = getters.decodedJWT
        const expirationTime = new Date(tokenInfo.exp * 1000)
        const timeNow = new Date()

        return timeNow < expirationTime
    }
}