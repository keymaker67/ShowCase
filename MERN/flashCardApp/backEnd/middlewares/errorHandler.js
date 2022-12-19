export function errorHandler (err, req, res) {
    console.log(err)
    res.status(500).json({msg: 'something went wrong, try again please!'})
}