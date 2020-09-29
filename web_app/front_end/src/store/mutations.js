export default {
    setData: (state, reviewMineData) => { state.reviewMinedData = reviewMineData },
    setJWT: (state, jwt) => { 
        state.currentJWT = jwt 
        localStorage.token = jwt
    }
}