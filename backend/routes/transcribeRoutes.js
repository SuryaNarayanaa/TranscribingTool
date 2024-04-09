const express = require('express')

const router= express.Router()

const transcribeController = require('../controllers/transcribeController.js')

router.route('/').get(transcribeController.getTranscript)




export default router