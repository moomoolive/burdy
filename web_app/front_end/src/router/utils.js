default export {
    isJWTValid: (state) => {
        const path = 'http://localhost:5000/authenticate'
        const payload = { token: state.currentJWT }
        axios.post(path, payload)
            .then((response) => {
                console.log(response)
                return true
            })
            .error((error) => {
                console.log(error)
                return false
            })
    }
}