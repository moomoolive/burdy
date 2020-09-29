import { delete } from 'vue/types/umd'
import state from './state.js'
import isValidJWT from '../utils/index.js'

export default {
    isAuthenticated: (state) => { isValidJWT(state.currentJWT) }
}