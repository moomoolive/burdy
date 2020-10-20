export default function sleep(ms) {
    // use with async function, put await infront of this function
    return new Promise(resolve => setTimeout(resolve, ms))
}