import state from './state.js'
import axios from 'axios'
import store from '../store/index.js'

export default {
    isLoggedIn: (state) => (!!state.currentJWT),
    // should split into two getters
    isJWTExpired: (state) => {
        const token = store.state.currentJWT
        if (!token || token.split('.').length < 3) {
            return true
        }
        const tokenInfo = atob(token.split('.')[1])
        const expirationTime = new Date(tokenInfo.exp * 1000)
        const timeNow = new Date()

        return timeNow < expirationTime
    }
}